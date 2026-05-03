#!/usr/bin/env python3
"""
PREDICCIÓN EN VIVO - Captura tráfico de red y detecta zero-days
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import models
import joblib
import time
import socket
import struct
from collections import deque

class LiveZeroDayDetector:
    def __init__(self, model_path='models/zero_day_autoencoder.h5', threshold_path='models/threshold.pkl'):
        self.model = models.load_model(model_path)
        self.threshold = joblib.load(threshold_path)
        self.buffer = deque(maxlen=50)
        
    def capture_packet(self):
        """Captura un paquete de red y extrae features"""
        # Simulación (en realidad usar scapy)
        return np.random.randn(78)  # 78 features
    
    def predict(self):
        """Predice si el tráfico actual es zero-day"""
        packet = self.capture_packet()
        self.buffer.append(packet)
        
        if len(self.buffer) == 50:
            sequence = np.array([self.buffer])
            reconstruction = self.model.predict(sequence, verbose=0)
            mse = np.mean(np.square(sequence - reconstruction))
            
            is_anomaly = mse > self.threshold
            confidence = min(100, (mse / self.threshold) * 100)
            
            return is_anomaly, confidence
        return False, 0
    
    def run_realtime(self):
        """Modo monitoreo en tiempo real"""
        print("[*] Monitoreando tráfico en tiempo real...")
        print("[*] Presiona Ctrl+C para detener\n")
        
        try:
            while True:
                is_anomaly, confidence = self.predict()
                if is_anomaly:
                    print(f"🚨 ZERO-DAY DETECTADO! Confianza: {confidence:.2f}%")
                else:
                    print(f"✅ Tráfico normal", end='\r')
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n\n[+] Monitoreo detenido")

if __name__ == "__main__":
    detector = LiveZeroDayDetector()
    detector.run_realtime()
