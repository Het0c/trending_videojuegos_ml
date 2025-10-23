import pandas as pd
import logging
   
logger = logging.getLogger(__name__)
  
def cargar_datos():
    df = pd.read_csv("data/01_raw/gaming.csv", parse_dates=["Date"])
    return df

def procesar_datos(df):
    df["dias"] = (df["Date"] - df["Date"].min()).dt.days
    return df

def calcular_estadisticas(df):
    media = df["Revenue"].mean()
    mediana = df["Revenue"].median()
    return {"media": media, "mediana": mediana}



def transformar_datos(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Iniciando transformación de datos")
    logger.info(f"Shape inicial: {df.shape}")

    # Convertir fecha
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Weekday"] = df["Date"].dt.day_name()

    # Crear nuevas features
    df["Purchases_per_user"] = df["In-game Purchases ($)"] / df["Daily Active Users (DAU)"]
    df["Engagement"] = df["Session Duration (minutes)"] * df["Daily Active Users (DAU)"]
    df["Social_Impact"] = df["Social Media Mentions"] + df["Influencer Endorsements"]

    # Codificar variables categóricas
    df = pd.get_dummies(df, columns=["Platform", "Top Genre"], drop_first=True)

    # Reordenar columnas (opcional)
    columnas_principales = [
        "Date", "Year", "Month", "Weekday", "Daily Active Users (DAU)",
        "New Registrations", "Session Duration (minutes)", "In-game Purchases ($)",
        "Revenue", "Purchases_per_user", "Engagement", "Social_Impact"
    ]
    columnas_finales = columnas_principales + [col for col in df.columns if col not in columnas_principales]
    df = df[columnas_finales]

    logger.info(f"Shape final: {df.shape}")
    logger.info("Transformación completada")

    return df
