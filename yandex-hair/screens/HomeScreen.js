import React from "react";

import { useTheme } from "@react-navigation/native";
import * as Animatable from "react-native-animatable";

import { ScrollView, StatusBar, StyleSheet, Text, View } from "react-native";
const HomeScreen = ({ navigation }) => {
  const theme = useTheme();

  return (
    <ScrollView style={styles.container}>
      <StatusBar barStyle={theme.dark ? "light-content" : "dark-content"} />
      <View style={styles.sliderContainer}>
        <View>
          <Text style={styles.text_header}>Welcome to Hairy Yandex!</Text>
          <View style={styles.header}>
            <Animatable.Image
              animation="bounceIn"
              duraton="1500"
              source={require("../assets/logo_cyan.png")}
              style={styles.logo}
              resizeMode="stretch"
            />
          </View>
          <Text style={styles.text}>
            For those who{" "}
            <Text style={[styles.text, { color: "#41b3ae" }]}>
              want to cut{" "}
              <Text style={[styles.text, { color: "#000" }]}>
                and for those who{" "}
                <Text style={[styles.text, { color: "#41b3ae" }]}>
                  want a to be cut!
                </Text>
              </Text>
            </Text>
          </Text>
        </View>
      </View>
    </ScrollView>
  );
};

export default HomeScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  sliderContainer: {
    width: "90%",
    marginTop: 30,
    justifyContent: "center",
    alignSelf: "center",
    borderRadius: 8,
  },
  text_header: {
    color: "#000",
    fontWeight: "bold",
    textAlign: "center",

    fontSize: 30,
  },
  text: {
    marginTop: 50,
    color: "#000",
    fontSize: 20,
    textAlign: "center",
  },
  logo: {
    width: 166,
    height: 191.5,
    alignSelf: "center",
    marginTop: 30,
  },
});
