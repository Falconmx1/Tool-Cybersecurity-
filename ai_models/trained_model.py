import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Dataset simulado de ataques (en realidad usarías CICIDS2017 o similar)
# Features: [bytes_in, bytes_out, duration, packets, flags, port, protocol]
X_train = np.array([
    # Tráfico normal
    [1024, 512, 0.5, 10, 2, 80, 6],
    [2048, 1024, 0.8, 20, 2, 443, 6],
    [512, 256, 0.3, 5, 2, 53, 17],
    
    # Ataques DDoS
    [100000, 50000, 60, 50000, 2, 80, 6],
    [200000, 100000, 120, 100000, 2, 443, 6],
    
    # Port scanning
    [64, 32, 0.1, 1000, 2, 22, 6],
    [128, 64, 0.2, 2000, 2, 23, 6],
    
    # Brute force
    [1500, 500, 300, 10000, 2, 22, 6],
    [1600, 600, 400, 15000, 2, 3389, 6],
])

y_labels = np.array([0,0,0,1,1,2,2,3,3])  # 0=normal, 1=ddos, 2=scan, 3=bruteforce

# Entrenar modelo
def train_cyber_ai():
    print("[+] Entrenando modelo de IA cibernética...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_scaled, y_labels)
    
    # Guardar modelo y scaler
    with open('ai_models/cyber_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('ai_models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print("[+] Modelo entrenado y guardado!")
    print(f"   - Accuracy: {model.score(X_scaled, y_labels)*100:.2f}%")
    return model, scaler

def predict_attack(features):
    """features = [bytes_in, bytes_out, duration, packets, flags, port, protocol]"""
    with open('ai_models/cyber_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('ai_models/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    features_scaled = scaler.transform([features])
    pred = model.predict(features_scaled)[0]
    
    attack_types = {0: "NORMAL ✅", 1: "DDoS 🚨", 2: "PORT SCAN 🔍", 3: "BRUTE FORCE 🔐"}
    print(f"[IA] Predicción: {attack_types[pred]}")
    return pred

# Ejecutar entrenamiento
if __name__ == "__main__":
    train_cyber_ai()
    
    # Prueba con tráfico real
    print("\n[TEST] Detectando ataque DDoS simulado...")
    predict_attack([150000, 75000, 45, 60000, 2, 80, 6])
