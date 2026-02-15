import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VehicleRecommender:

    def __init__(self):
        self.data=pd.DataFrame({
            "name":[
                "Hyundai Creta","Honda City","Toyota Fortuner","Maruti Swift",
                "Royal Enfield 350","KTM Duke 390","Honda Activa","TVS Apache 160"
            ],
            "type":[
                "Car","Car","Car","Car",
                "Bike","Bike","Scooter","Bike"
            ],
            "features":[
                "SUV Petrol Diesel Family",
                "Sedan Petrol Family",
                "SUV Diesel Luxury",
                "Hatchback Petrol Budget",
                "Cruiser Petrol",
                "Sports Petrol",
                "Scooter Petrol Budget",
                "Sports Petrol Budget"
            ]
        })
        self.vectorizer=TfidfVectorizer()
        self.tfidf_matrix=self.vectorizer.fit_transform(self.data["features"])

    def recommend(self,user_preferences,top_n=5):
        user_vector=self.vectorizer.transform([user_preferences])
        similarity=cosine_similarity(user_vector,self.tfidf_matrix)
        scores=list(enumerate(similarity[0]))
        sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
        recommendations=[self.data.iloc[i]["name"] for i,_ in sorted_scores[:top_n]]
        return recommendations

def main():
    recommender=VehicleRecommender()
    user_input=input("Enter preferences (e.g., Budget Petrol SUV Sports Family): ").strip()
    if not user_input:
        print("Please enter valid preferences.")
        return
    results=recommender.recommend(user_input,top_n=5)
    print("\nTop Recommended Vehicles:\n")
    for idx,vehicle in enumerate(results,1):
        print(f"{idx}. {vehicle}")

if __name__=="__main__":
    main()
