import React from 'react';
import { View, Text, StyleSheet, FlatList, Image, TouchableOpacity } from 'react-native';
import { useRoute, RouteProp, useNavigation } from '@react-navigation/native';

type RootStackParamList = {
  Home: undefined;
  Articles: { category: string };
};

type ArticlesScreenRouteProp = RouteProp<RootStackParamList, 'Articles'>;

const articles = [
  {
    id: '1',
    title: 'Article 1',
    image: require('../assets/icon.png'),
  },
  {
    id: '2',
    title: 'Article 2',
    image: require('../assets/icon.png'),
  },
  // Add more articles as needed
];

const ArticlesScreen: React.FC = () => {
  const route = useRoute<ArticlesScreenRouteProp>();
  const { category } = route.params;
  const navigation = useNavigation();

  const renderItem = ({ item }: { item: typeof articles[number] }) => (
    <View style={styles.articleBox}>
      <Image source={item.image} style={styles.articleImage} />
      <Text style={styles.articleTitle}>{item.title}</Text>
    </View>
  );

  const handleGoBack = () => {
    navigation.goBack();
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>{category}</Text>
      <FlatList
        data={articles}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
      />
      <TouchableOpacity style={styles.goBackButton} onPress={handleGoBack}>
        <Text style={styles.goBackText}>Go Back</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingHorizontal: 20,
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginVertical: 20,
    fontFamily: 'CircularStd-Bold', // Use the custom font
  },
  articleBox: {
    marginBottom: 20,
  },
  articleImage: {
    width: '100%',
    height: 200,
    borderRadius: 10,
  },
  articleTitle: {
    fontSize: 18,
    marginVertical: 10,
    fontFamily: 'CircularStd-Medium', // Use the custom font
  },
  goBackButton: {
    alignSelf: 'center',
    marginTop: 20,
    padding: 10,
    backgroundColor: '#ccc',
    borderRadius: 5,
  },
  goBackText: {
    fontSize: 18,
    fontFamily: 'CircularStd-Bold', // Use the custom font
  },
});

export default ArticlesScreen;
