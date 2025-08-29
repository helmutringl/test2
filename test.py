import requests

print("Teste Verbindung zu einer alternativen API (open-meteo.com)...")
try:
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.21&longitude=16.37&current_weather=true"
    response = requests.get(url)
    response.raise_for_status() # Prüft auf Fehler wie 4xx oder 5xx

    # Wenn der Code hier ankommt, war die Anfrage erfolgreich
    print("✅ Erfolgreich! Antwort vom Server erhalten:")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"❌ Fehler: Konnte den alternativen Server nicht erreichen. Problem: {e}")