import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { NativeStackNavigationProp } from '@react-navigation/native-stack';

type RootStackParamList = {
  Home: undefined;
  Articles: { category: string };
};

type HomeScreenNavigationProp = NativeStackNavigationProp<RootStackParamList, 'Home'>;

const HomeScreen: React.FC = () => {
  const navigation = useNavigation<HomeScreenNavigationProp>();

  const handlePress = (category: string) => {
    navigation.navigate('Articles', { category });
  };

  const renderTextWithBox = (firstWord: string, secondWord: string, color: string) => (
    <TouchableOpacity style={styles.button} onPress={() => handlePress(`${firstWord} ${secondWord}`)}>
      <Text style={styles.text}>{firstWord} </Text>
      <View style={[styles.box, { backgroundColor: color }]}>
        <Text style={styles.textBox}>{secondWord}</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      {renderTextWithBox('Rafah', 'Bombing', '#2D2C2C')}
      {renderTextWithBox('Campus', 'Protesting', '#314CDE')}
      {renderTextWithBox('Brazil', 'Floods', '#CF6021')}
      {renderTextWithBox('US', 'Elections', '#D05050')}
      {renderTextWithBox('Disney', 'Stocks', '#EBBF4E')}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'flex-start', // Align items to the start (left)
    backgroundColor: '#fff',
    paddingHorizontal: 20, // Add horizontal padding to center content better
  },
  button: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 0,
  },
  text: {
    fontSize: 40,
    color: '#202020',
    fontFamily: 'CircularStd-Bold', // Use the custom font
  },
  box: {
    padding: 5,
  },
  textBox: {
    fontSize: 40,
    color: '#fff', // Set text color to white
    fontFamily: 'CircularStd-Bold', // Use the custom font
  },
});

export default HomeScreen;
