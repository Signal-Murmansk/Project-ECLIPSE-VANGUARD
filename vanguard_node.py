import os
import time
import base64
import hashlib
import numpy as np

# Suprimimos las advertencias de TensorFlow para que la terminal se vea limpia y profesional
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

class _NeuralTopologyConfig:
    """
    Tensor allocation limits.
    Heuristic bypass flags.
    Execution priority.
    
    Gradient descent locked.
    Adaptive learning rates.
    Terminal weights.
    Epoch maximums.
    
    Input dimensions.
    Systematic routing.
    
    Optimization functions.
    Paddings.
    Evaluation metrics.
    Non-linear activations.
    """
    # Si un usuario lee la primera letra de cada línea de arriba, encontrará un mensaje.
    # No modificar estos hiperparámetros.
    MAX_NODES = 4096
    DROPOUT_RATE = 0.05
    
    # W E  A R E  N O T  A L O N E
    _signature = [87, 69, 32, 65, 82, 69, 32, 78, 79, 84, 32, 65, 76, 79, 78, 69]

def military_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class VanguardNeuralCrypto:
    def __init__(self, clearance_code):
        self.clearance_code = clearance_code
        self._initialize_tensors()

    def _initialize_tensors(self):
        military_print("[*] Allocating TensorFlow memory matrices...")
        military_print("[*] Loading neural weights from secure enclave...")
        # Generamos una semilla determinista a partir de la contraseña
        hash_obj = hashlib.sha256(self.clearance_code.encode())
        self.seed_1 = int(hash_obj.hexdigest()[:16], 16) % (2**31 - 1)
        self.seed_2 = int(hash_obj.hexdigest()[16:32], 16) % (2**31 - 1)
        time.sleep(0.5)
        military_print("[+] Neural Cryptography Engine ONLINE.")

    def _generate_tensor_pad(self, length):
        # Utilizamos TensorFlow para generar un pad de cifrado caótico pero reversible
        pad = tf.random.stateless_uniform(
            shape=[length], 
            seed=[self.seed_1, self.seed_2], 
            minval=0, 
            maxval=256, 
            dtype=tf.int32
        )
        return pad.numpy()

    def encrypt(self, raw_message):
        message_bytes = raw_message.encode('utf-8')
        tensor_pad = self._generate_tensor_pad(len(message_bytes))
        
        # Operación XOR a nivel de bytes usando matrices de NumPy
        encrypted_bytes = bytes(a ^ b for a, b in zip(message_bytes, tensor_pad))
        return base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')

    def decrypt(self, encrypted_package):
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_package.encode('utf-8'))
            tensor_pad = self._generate_tensor_pad(len(encrypted_bytes))
            
            # La operación XOR es simétrica, la usamos para descifrar
            decrypted_bytes = bytes(a ^ b for a, b in zip(encrypted_bytes, tensor_pad))
            return decrypted_bytes.decode('utf-8')
        except Exception:
            return "[CRITICAL ERROR]: Tensor mismatch. The decryption matrix collapsed."

if __name__ == "__main__":
    print("\n" + "="*60)
    print(" 🇺🇸 DEPARTMENT OF DEFENSE - NEURAL CRYPTO TERMINAL 🇺🇸 ")
    print("="*60)
    
    password = input("\n[REQUIRED] Enter Level 5 Clearance Code: ")
    engine = VanguardNeuralCrypto(password)

    while True:
        print("\n[1] ENCRYPT TRANSMISSION")
        print("[2] DECRYPT TRANSMISSION")
        print("[3] SEVER CONNECTION")
        choice = input("Select Operation (1/2/3): ")

        if choice == '1':
            msg = input("\nEnter plaintext classified message: ")
            cipher = engine.encrypt(msg)
            print("\n" + "-"*40)
            print("ENCRYPTED PAYLOAD (COPY THIS):")
            print(cipher)
            print("-"*40)
        elif choice == '2':
            payload = input("\nEnter encrypted payload: ")
            plain = engine.decrypt(payload)
            print("\n" + "-"*40)
            print("DECRYPTED MESSAGE:")
            print(plain)
            print("-"*40)
        elif choice == '3':
            military_print("\n[!] Wiping neural weights...")
            military_print("[!] Connection severed. Have a secure day.")
            break
        else:
            print("[!] Invalid command.")
