# Copyright (c) 2025-2026 K.N.Narin (github.com/narin-kura). All rights reserved.
# Non-commercial use only. Commercial use requires written permission: github.com/narin-kura
# See LICENSE for full terms.
"""Supabase auth: JWT verification + service-role client for personalization data."""

from __future__ import annotations
import logging
import os
from typing import Optional

import jwt
from jwt import PyJWKClient
from fastapi import Header, HTTPException
from supabase import create_client, Client

logger = logging.getLogger(__name__)

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY", "")
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")

supabase: Optional[Client] = None
jwks_client: Optional[PyJWKClient] = None
SUPABASE_CONFIGURED = bool(SUPABASE_URL and SUPABASE_SERVICE_KEY)

if SUPABASE_CONFIGURED:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
        jwks_client = PyJWKClient(f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json", cache_keys=True)
    except Exception:
        logger.exception("Failed to create Supabase client — personalization endpoints disabled")
        SUPABASE_CONFIGURED = False
else:
    logger.warning("Supabase env vars not set — personalization endpoints disabled")


async def get_current_user(authorization: str = Header(default="")) -> str:
    """Verify a Supabase access token (ES256/RS256 via JWKS) and return the user id (sub claim)."""
    if not SUPABASE_CONFIGURED:
        raise HTTPException(503, "Personalization is not configured on this server")
    if not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing or invalid Authorization header")
    token = authorization[len("Bearer "):].strip()
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["ES256", "RS256"],
            audience="authenticated",
        )
    except jwt.PyJWTError as e:
        raise HTTPException(401, f"Invalid token: {e}")
    sub = payload.get("sub")
    if not sub:
        raise HTTPException(401, "Token missing subject")
    return sub
