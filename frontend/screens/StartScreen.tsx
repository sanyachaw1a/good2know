import React from 'react';
import { View, Button, Image, StyleSheet, TouchableOpacity } from 'react-native';
import { NativeStackNavigationProp } from '@react-navigation/native-stack';
import { RootStackParamList } from '../types';
import { Ionicons } from '@expo/vector-icons'; // Import Ionicons for the arrow icon


type StartScreenProps = {
  navigation: NativeStackNavigationProp<RootStackParamList, 'Start'>;
};

const StartScreen: React.FC<StartScreenProps> = ({ navigation }) => {
  const handleButtonPress = () => {
    navigation.navigate('Home');
  };

  return (
    <View style={styles.container}>
      <View style={styles.innerContainer}>
        <Image source={require('../assets/logo.png')} style={styles.logo} />
        <TouchableOpacity style={styles.button} onPress={handleButtonPress}>
            <Ionicons name="arrow-forward" size={24} color="#fff" />
      </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff', // Set white background color
  },
  innerContainer: {
    marginLeft: 50,
    marginTop: 100
  },
  logo: {
    width: 420,
    height: 380,
    marginBottom: 20,
  },
  button: {
    width: 50,
    height: 50,
    borderRadius: 25, // Make the button circular
    backgroundColor: '#314CDE', // Change the background color of the button
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 340,
  },
});

export default StartScreen;
