import React, { useState } from "react";
import {
  View,
  Text,
  Button,
  TouchableOpacity,
  Dimensions,
  TextInput,
  Platform,
  StyleSheet,
  ScrollView,
  StatusBar,
} from "react-native";
import { LinearGradient } from "expo-linear-gradient";
import { Picker } from "@react-native-picker/picker";
import DateTimePicker from "@react-native-community/datetimepicker";

const CreateEventScreen = ({ navigation }) => {
  const [data, setData] = React.useState({
    startTime: new Date(),
    endTime: new Date(),
    name: "Test event",
    description: "Test event",
    address: "TestEvent",
    category: "Short",
  });

  const titleInputChange = (val) => {
    if (val.length !== 0) {
      setData({
        ...data,
        name: val,
      });
    }
  };

  const handleCategory = (val) => {
    setData({
      ...data,
      category: val,
    });
  };

  const setStartTime = (val) => {
    console.log(val);
    // setData({
    //     ...data,
    //     startTime: new Date(val)
    // });
  };

  const setEndTime = (val) => {
    setData({
      ...data,
      endTime: new Date(val),
    });
  };

  const handleSubmit = async () => {
    console.log(data);
    await createEvent({
      lat: data.lat,
      lng: data.long,
      startTime: data.startTime,
      endTime: data.endTime,
      name: data.name,
      description: data.description,
      address: data.address,
      category: data.category,
    }).catch((error) => console.log(error));
  };

  const [isPickerShow, setIsPickerShow] = useState(true);
  const [date, setDate] = useState(new Date(Date.now()));

  const showPicker = () => {
    setIsPickerShow(true);
  };

  const onChange = (event, value) => {
    setDate(value);
    if (Platform.OS === "android") {
      setIsPickerShow(false);
    }
  };

  const [category, setCategory] = useState("Short");
  return (
    <View style={styles.container}>
      <StatusBar backgroundColor="#FF6347" barStyle="light-content" />
      <View style={styles.header}>
        <Text style={styles.text_header}>Create Appointment</Text>

        <TextInput
          placeholder="Service"
          style={styles.textInput}
          onChangeText={(val) => titleInputChange(val)}
        />

        <Picker
          selectedValue={category}
          onValueChange={(currentCategory) => {
            setCategory(currentCategory);
            console.log(currentCategory);
          }}
          style={styles.selectPicker}
        >
          <Picker.Item label="Short" value="Short" />
          <Picker.Item label="Medium" value="Medium" />
          <Picker.Item label="Long" value="Long" />
        </Picker>

        {!isPickerShow && (
          <View style={styles.btnContainer}>
            <Button title="Show Picker" color="purple" onPress={showPicker} />
          </View>
        )}
        <Text style={styles.text}>Date and Time:</Text>
        {/* The date picker */}
        {isPickerShow && (
          <DateTimePicker
            value={data.startTime}
            mode={"datetime"}
            display={Platform.OS === "ios" ? "spinner" : "default"}
            is24Hour={false}
            onChange={(event, value) => setData({ ...data, startTime: value })}
            style={styles.datePicker}
          />
        )}

        <View style={styles.button}>
          <TouchableOpacity style={styles.signIn} onPress={handleSubmit}>
            <LinearGradient
              colors={["#e8a87c", "#e8a87c"]}
              style={styles.signIn}
            >
              <Text
                style={[
                  styles.textSign,
                  {
                    color: "#fff",
                  },
                ]}
              >
                Submit
              </Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
};

export default CreateEventScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
  },
  header: {
    flex: 1,
    paddingHorizontal: 20,
    paddingTop: 80,
  },
  footer: {
    flex: Platform.OS === "ios" ? 3 : 5,
    backgroundColor: "#fff",
    borderTopLeftRadius: 30,
    borderTopRightRadius: 30,
    paddingHorizontal: 20,
    paddingVertical: 30,
  },
  text_header: {
    color: "#000",
    fontWeight: "bold",
    fontSize: 30,
  },
  text: {
    marginTop: 20,
    color: "#000",
    fontSize: 20,
  },
  text_footer: {
    color: "#000",
    fontSize: 25,
  },
  action: {
    flexDirection: "row",
    marginTop: 10,
    borderBottomWidth: 1,
    borderBottomColor: "#f2f2f2",
    paddingBottom: 5,
  },
  text_input: {
    flex: 1,
    marginTop: Platform.OS === "ios" ? 0 : -12,
    paddingLeft: 10,
    color: "#000",
  },
  textInput: {
    paddingLeft: 20,
    paddingTop: 15,
    fontSize: 20,
    paddingBottom: 10,
    color: "#000",
  },
  button: {
    alignItems: "center",
    marginTop: 10,
  },
  signIn: {
    width: "100%",
    height: 50,
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 10,
  },
  textSign: {
    fontSize: 18,
    fontWeight: "bold",
  },
  textPrivate: {
    flexDirection: "row",
    flexWrap: "wrap",
    marginTop: 20,
  },
  color_textPrivate: {
    color: "grey",
  },
  datePicker: {
    height: 80,
    display: "flex",
    justifyContent: "center",
    alignItems: "flex-start",
  },
  selectPicker: {
    height: 50,
    display: "flex",
    paddingBottom: 200,
  },
});
