import React from "react";
import { View, SafeAreaView, StyleSheet } from "react-native";
import { Avatar, Title, Text, TouchableRipple } from "react-native-paper";

import Icon from "react-native-vector-icons/MaterialCommunityIcons";

import files from "../assets/filesBase64";

const ProfileScreen = () => {
  const myCustomShare = async () => {
    const shareOptions = {
      message:
        "Find intersting events on FindMe. I've already paricipated in 5 of them.",
      url: files.appLogo,
      urls: [files.image1, files.image2],
    };

    try {
      const ShareResponse = await Share.open(shareOptions);
      console.log(JSON.stringify(ShareResponse));
    } catch (error) {
      console.log("Error => ", error);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.userInfoSection}>
        <View style={{ flexDirection: "row", marginTop: 15 }}>
          <Avatar.Image source={require("../assets/mad.png")} size={80} />
          <View style={{ marginLeft: 20 }}>
            <Title
              style={[
                styles.title,
                {
                  marginTop: 25,
                  marginBottom: 5,
                },
              ]}
            >
              Madonna Donna
            </Title>
          </View>
        </View>
      </View>

      <View style={styles.userInfoSection}>
        <View style={styles.row}>
          <Icon name="map-marker-radius" color="#000" size={20} />
          <Text style={{ color: "#000", marginLeft: 20 }}>Chișinău</Text>
        </View>
        <View style={styles.row}>
          <Icon name="phone" color="#000" size={20} />
          <Text style={{ color: "#000", marginLeft: 20 }}>060270000</Text>
        </View>
        <View style={styles.row}>
          <Icon name="email" color="#000" size={20} />
          <Text style={{ color: "#000", marginLeft: 20 }}>
            madodonna@mail.notru
          </Text>
        </View>
      </View>

      <View style={styles.menuWrapper}>
        <TouchableRipple onPress={() => {}}>
          <View style={styles.menuItem}>
            <Icon name="calendar" color="#e8a87c" size={25} />
            <Text style={styles.menuItemText}>Your Appointments</Text>
          </View>
        </TouchableRipple>
        <TouchableRipple onPress={() => {}}>
          <View style={styles.menuItem}>
            <Icon name="account" color="#e8a87c" size={25} />
            <Text style={styles.menuItemText}>Clients</Text>
          </View>
        </TouchableRipple>
        <TouchableRipple onPress={myCustomShare}>
          <View style={styles.menuItem}>
            <Icon name="share-outline" color="#e8a87c" size={25} />
            <Text style={styles.menuItemText}>Share</Text>
          </View>
        </TouchableRipple>
      </View>
    </SafeAreaView>
  );
};

export default ProfileScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  userInfoSection: {
    paddingHorizontal: 30,
    marginBottom: 25,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
  },
  caption: {
    fontSize: 14,
    lineHeight: 14,
    fontWeight: "500",
  },
  row: {
    flexDirection: "row",
    marginBottom: 10,
  },
  infoBoxWrapper: {
    borderBottomColor: "#dddddd",
    borderBottomWidth: 1,
    borderTopColor: "#dddddd",
    borderTopWidth: 1,
    flexDirection: "row",
    height: 100,
  },
  infoBox: {
    width: "50%",
    alignItems: "center",
    justifyContent: "center",
  },
  menuWrapper: {
    marginTop: 10,
  },
  menuItem: {
    flexDirection: "row",
    paddingVertical: 15,
    paddingHorizontal: 30,
  },
  menuItemText: {
    color: "#777777",
    marginLeft: 20,
    fontWeight: "600",
    fontSize: 16,
    lineHeight: 26,
  },
});
