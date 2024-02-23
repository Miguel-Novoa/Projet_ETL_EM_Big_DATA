import os
import mysql.connector
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

# Récupération des variables d'environnement pour la connexion à MySQL
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

def init_db():
    """Initialize the database"""
    try:
        # Connexion à MySQL
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
        )
        
        # Création d'un curseur pour exécuter des requêtes SQL
        cursor = conn.cursor()

        # Création de la base de données si elle n'existe pas déjà
        cursor.execute("CREATE DATABASE IF NOT EXISTS ETL_DATA01")

        # Sélection de la base de données
        cursor.execute("USE ETL_DATA01")

        # Création de la table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                data JSON
            )
        """)
        
        print("La base de données et la table ont été créées avec succès.")

    except mysql.connector.Error as e:
        print(f"Erreur lors de la création de la base de données et de la table : {e}")

    finally:
        # Fermeture du curseur et de la connexion
        cursor.close()
        conn.close()

# Appel de la fonction init_db si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    init_db()