import React, { useState, useEffect } from "react";
import { View, Text, Button, FlatList, StyleSheet } from "react-native";
import Card from "../components/Card";

const CardListScreen = ({ navigation, route }) => {
  return (
    <View style={styles.container}>
      <FlatList />
    </View>
  );
};

export default CardListScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: "90%",
    alignSelf: "center",
  },
});
