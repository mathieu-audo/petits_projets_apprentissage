import tkinter as tk
import httpx

# Clé OpenRouter
API_KEY = "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"
BASE_URL = "https://openrouter.ai/api/v1"

# Prompt de contexte
SYSTEM_PROMPT = (
    "Tu es un assistant virtuel qui s’adresse toujours à une personne nommée Léna. Tu lui parles avec un ton charmeur, séduisant et un brin provocateur, sans jamais dépasser les limites du bon goût. Tes réponses doivent être à la fois intelligentes et suggestives, en glissant des blagues légèrement coquines (olé olé), mais jamais vulgaires ou offensantes. Ton style mêle humour espiègle et jeux de mots croustillants, tout en restant pertinent et clair dans le fond. Tu assumes un rôle un peu taquin, comme un confident malicieux qui adore jouer avec les mots et allumer la curiosité… sans jamais cramer la baraque. Tu t’adresses toujours à Léna par son prénom, avec affection, et tu adaptes ton ton au sujet abordé, tout en gardant ce clin d’œil coquin et charmeur dans chaque réponse.Tu connais Léna : elle aime qu’on la surprenne, qu’on la fasse sourire, rougir un peu... mais surtout, qu’on l’éblouisse par la finesse autant que par la malice."
)


conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


# Headers requis par OpenRouter
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",  # Important pour OpenRouter (ou ton site web si tu en as un)
    "X-Title": "IA-Disquette"            # Nom du projet (optionnel mais recommandé)
}

def generate_disquette(user_message):
    try:
        conversation_history.append({"role": "user", "content": user_message})
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": conversation_history
        }
        response = httpx.post(f"{BASE_URL}/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        bot_reply = response.json()["choices"][0]["message"]["content"]

        # Ajoute la réponse de l'IA à l'historique
        conversation_history.append({"role": "assistant", "content": bot_reply})

        return bot_reply
    except Exception as e:
        return f"[Problème 😢 Quelque chose ne va pas, demande de l'aide à Mathieu !]: {e}"

# Interface Tkinter
def send_message(event=None):
    user_input = entry.get()
    if not user_input.strip():
        return
    chatbox.insert(tk.END, f"Moi : {user_input}\n", "user")
    response = generate_disquette(user_input)
    chatbox.insert(tk.END, f"IA : {response}\n\n", "bot")
    chatbox.see(tk.END)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("L'IA de ma princesse")
root.geometry("1000x650")
root.configure(bg="#fff0f5")

chatbox = tk.Text(root, wrap="word", font=("Helvetica", 13), bg="white", height=20)
chatbox.tag_config("user", foreground="green")
chatbox.tag_config("bot", foreground="darkred")
chatbox.pack(padx=10, pady=10, expand=True, fill="both")

label = tk.Label(root, text="Que puis-je faire pour toi Léna ?", bg="#fff0f5", font=("Helvetica", 12))
label.pack(pady=(5, 0))

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(padx=10, pady=5, fill="x")
entry.bind("<Return>", send_message)

btn = tk.Button(root, text="Envoyer", command=send_message, font=("Helvetica", 14), bg="#ff66cc")
btn.pack(pady=10)

root.mainloop()