import firebase_admin
from firebase_admin import credentials, firestore
import forloop
import groqApi

# Initialize Firebase Admin SDK
cred = credentials.Certificate("buzz-a3a35-firebase-adminsdk-pjnpq-a7fb37a17d.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Assuming your top_five_groups is already defined as per your code above
top_five_groups = forloop.top_five_groups

# Function to replace data in Firestore
def replace_groups_in_firestore(groups):
    # Delete all existing documents in the 'groups' collection
    docs = db.collection('groups').stream()
    for doc in docs:
        doc.reference.delete()
    
    # Add new data
    for i, (group, intersecting_words, avg_importance) in enumerate(groups):
        group_title = groqApi.generate_title(intersecting_words).strip()[1:-1]
        group_data = {
            'title': group_title,
            'average_importance': avg_importance,
            'articles': []
        }
        
        for article in group:
            article_data = {
                'source': article.source,
                'url': article.url,
                'title': article.title,
                'img_source': article.img_source
            }
            group_data['articles'].append(article_data)
        
        db.collection('groups').add(group_data)

# Replace data in Firestore with top five groups
replace_groups_in_firestore(top_five_groups)
