import { Stack } from "expo-router";
import { StatusBar } from "expo-status-bar";
import { Colors } from "../constants/Colors";

export default function RootLayout() {
  return (
    <>
      <StatusBar style="light" />
      <Stack
        screenOptions={{
          headerStyle: { backgroundColor: Colors.primary },
          headerTintColor: "#fff",
          headerTitleStyle: { fontWeight: "700" },
          contentStyle: { backgroundColor: Colors.background },
        }}
      >
        <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
        <Stack.Screen
          name="career/[id]"
          options={{ title: "Career Details", headerBackTitle: "Back" }}
        />
        <Stack.Screen
          name="feedback"
          options={{ title: "Feedback", headerBackTitle: "Back" }}
        />
      </Stack>
    </>
  );
}
