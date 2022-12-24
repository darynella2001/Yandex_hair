import React from "react";
import {
  View,
  Text,
  TouchableOpacity,
  Dimensions,
  StyleSheet,
  StatusBar,
  Image,
} from "react-native";
import * as Animatable from "react-native-animatable";
import { LinearGradient } from "expo-linear-gradient";
import { useTheme } from "@react-navigation/native";

const SplashScreen = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <StatusBar backgroundColor="#FF6347" barStyle="light-content" />
      <View style={styles.header}>
        <Animatable.Image
          animation="bounceIn"
          duraton="1500"
          source={require("../assets/logo_cyan.png")}
          style={styles.logo}
          resizeMode="stretch"
        />
      </View>
      <Animatable.View
        style={[
          styles.footer,
          {
            backgroundColor: "#fff",
          },
        ]}
        animation="fadeInUpBig"
      >
        <Text
          style={[
            styles.title,
            {
              color: "#41b3ae",
            },
          ]}
        >
          Get your hair done!
        </Text>
        {/* <Text style={styles.text}>Sign in with existing account</Text> */}
        <View style={styles.button}>
          <TouchableOpacity onPress={() => navigation.navigate("SignInScreen")}>
            <LinearGradient
              colors={["#ffd500", "#ffd500"]}
              style={styles.signIn}
            >
              <Text style={styles.textSign}>Get Started</Text>
              {/* <MaterialIcons name="navigate-next" color="#000" size={20} /> */}
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </Animatable.View>
    </View>
  );
};

export default SplashScreen;

const { height } = Dimensions.get("screen");
const height_logo = height * 0.25;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  header: {
    flex: 2,
    justifyContent: "center",
    alignItems: "center",
  },
  footer: {
    flex: 1,
    backgroundColor: "#5ea",
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
    borderBottomLeftRadius: 20,
    borderBottomRightRadius: 20,
    marginLeft: 10,
    marginRight: 10,
    marginBottom: 60,
    paddingVertical: 30,
    paddingHorizontal: 30,
  },
  logo: {
    width: 199.2,
    height: 229.8,
  },
  title: {
    color: "#000",
    fontSize: 35,
    fontWeight: "bold",
  },

  button: {
    justifyContent: "center",
    alignItems: "center",
    marginTop: 30,
  },
  signIn: {
    width: 150,
    height: 40,
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 50,
    flexDirection: "row",
  },
  textSign: {
    color: "#000",
    fontWeight: "bold",
  },
});
