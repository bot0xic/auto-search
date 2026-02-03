import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time, random, tempfile

SEARCH_LIST = [
    "Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Erling Haaland", "Neymar Jr",
    "Kevin De Bruyne", "Robert Lewandowski", "Mohamed Salah", "Harry Kane", "Vinícius Júnior",
    "Luka Modrić", "Karim Benzema", "Jude Bellingham", "Bukayo Saka", "Phil Foden",
    "Son Heung-min", "Bruno Fernandes", "Antoine Griezmann", "Martin Ødegaard", "João Félix",
    "Pedri", "Gavi", "Jadon Sancho", "Declan Rice", "Kai Havertz","Alisson Becker",
    "Joshua Kimmich", "Alphonso Davies","Andrew Robertson", "Reece James", "Ederson Moraes", "Frenkie de Jong", "Ilkay Gündogan", "Trent Alexander-Arnold", "Bruno Fernandes", "Antoine Griezmann",
    "Marcus Rashford", "Sadio Mané", "Riyad Mahrez", "Lautaro Martínez", "Christian Pulisic",
    "Mason Mount", "Thiago Alcântara", "Casemiro", "Toni Kroos", "Raphaël Varane",
    "Virgil van Dijk", "Sergio Ramos", "Kalidou Koulibaly", "Achraf Hakimi", "João Cancelo",
    "Theo Hernández", "Andrew Robertson", "Reece James", "Ederson Moraes", "Alisson Becker", 
    "Bruno Fernandes", "Antoine Griezmann", "Martin Ødegaard", "João Félix","Karim Benzema",
    "Andrew Robertson" ,"How to learn Python quickly?","How to fix a slow computer?",
    "How to install Selenium in Python?","How to make a website using HTML and CSS?","How to scrape data from a website safely?",
    "How to automate browser tasks using Python?","How to use ChatGPT for coding help?","How to protect my computer from viruses?",
    "How to backup my data to the cloud?","How to improve Wi-Fi speed?","How to focus while studying?","How to remember what I study for exams?",
    "How to take better notes in class?","How to write a research paper?","How to summarize a long text easily?",
    "How to write a good CV or résumé?", "How to prepare for a job interview?","How to manage time effectively?","How to stay motivated at work?",
    "How to set and achieve goals?","How to save money every month?","How to start an online business?","How to make money using freelancing?",
    "How to invest safely as a beginner?","How to create a business plan?","How to speak confidently in public?",
    "How to control stress and anxiety?", "How to build good habits?","How to stay healthy and fit?","How to make new friends easily?","How does artificial intelligence impact future employment opportunities and job markets across different industries globally within the next two decades?",
    "Why do some businesses succeed in brand loyalty creation while others fail even when offering similar quality products and competitive prices?",
    "What are the psychological effects of social media usage on teenagers and young adults in the long-term over several years of daily exposure?",
    "How can renewable energy sources like solar and wind reduce climate change impact if adopted in at least 60% of countries worldwide?",
    "What are the strongest factors that influence online consumer trust when buying from newly launched e-commerce stores with no physical presence?",
    "How do video games affect children’s brain development positively or negatively depending on the type, duration, and content they interact with?",
    "Why do humans procrastinate important tasks even when they fully understand the long-term benefits of finishing work earlier or on time?",
    "How do cryptocurrencies and blockchain technology change the global banking and finance systems in the next ten to fifteen years?",
    "What are the most effective studying techniques proven by scientific research that can improve memory retention for students preparing for exams?",
    "Why do some people become better leaders than others even when both groups receive similar education, training, and development opportunities?",
    "How does sleep quality influence problem solving abilities, concentration level, and creativity performance during work or study the next day?",
    "What are the most common mistakes new entrepreneurs make during their first startup attempt and how can those mistakes be avoided?",
    "How do factors like culture, environment, and family values shape a person’s long-term belief system and behavior patterns in adult life?",
    "Why do humans enjoy watching horror movies even though the content triggers fear, danger signals, and stress hormones inside the brain?",
    "How does language shape the way people think differently in society depending on vocabulary, grammar structures, and cultural metaphors?",
    "What are the main future dangers of depending heavily on robots and automation inside hospitals, transportation, factories, and daily life?",
    "How can developing emotional intelligence help improve communication, conflict handling, and relationship stability both in workplace and personal life?",
    "Why does music have the power to change human mood quickly and influence feelings like sadness, happiness, motivation, or calmness instantly?",
    "How does exercise affect mental health and why do doctors recommend sports as part of treatment for stress and anxiety reduction?",
    "Why do people form addictions to mobile phones and what are the consequences of continuous dopamine seeking behavior through notifications?",
    "How do marketing advertisements influence decision making unconsciously even when the customer believes they are making completely logical choices?",
    "What are the most important reasons behind failures of long-distance relationships and which behaviors increase chances of relationship survival?",
    "Why do some students learn faster than others even if they spend less time studying and less effort during regular practice sessions?",
    "How can humans improve memory power and store more information permanently by using natural techniques instead of artificial medications?",
    "Why do people fear public speaking more than many physical dangers even though public speaking cannot actually physically hurt them?",
    "How will future smart home systems with AI change daily living lifestyle and reduce time spent doing basic household tasks and routines?",
    "How can governments reduce the level of corruption inside organizations and build trust between citizens and public service institutions again?",
    "What are the best ways for parents to teach their children financial responsibility so they don’t face major money problems in adulthood?",
    "Why does traveling to different countries improve personality development, understanding of cultures, emotional acceptance, and global thinking perspective?",
    "How can machine learning detect early signs of dangerous diseases before symptoms appear, potentially increasing survival rates for millions of patients?","What are the health benefits of a Mediterranean diet compared to other popular diets like keto or paleo in long-term studies?",
    "How does climate change specifically impact marine biodiversity and what are the potential consequences for global ecosystems?",
    "What p advancements in quantum computing threaten current encryption methods and what new security measures can be implemented?",
    "What role does gut microbiota play in mental health disorders such as depression and anxiety according to recent scientific research?",
    "How can urban planning and architecture be optimized to promote sustainable living and reduce carbon footprints in major cities?",
    "What are the ethical implications of using CRISPR technology for human genetic modification and where should regulatory boundaries be set?",
    "How do cultural differences influence communication styles in international business negotiations and what strategies can improve outcomes?",
    "What are the long-term effects of space travel on human physiology and how can astronauts mitigate these risks during extended missions?",
    "How does exposure to nature and green spaces contribute to cognitive development and emotional well-being in children and adults alike?",
    "What are the most important reasons behind failures of long-distance relationships and which behaviors increase chances of relationship survival?",
    "Why do some students learn faster than others even if they spend less time studying and less effort during regular practice sessions?",
    "How can humans improve memory power and store more information permanently by using natural techniques instead of artificial medications?",
    "Why do people fear public speaking more than many physical dangers even though public speaking cannot actually physically hurt them?",
    "How will future smart home systems with AI change daily living lifestyle and reduce time spent doing basic household tasks and routines?",
    "How can governments reduce the level of corruption inside organizations and build trust between citizens and public service institutions again?",
    "What are the best ways for parents to teach their children financial responsibility so they don’t face major money problems in adulthood?",
    "Why does traveling to different countries improve personality development, understanding of cultures, emotional acceptance, and global thinking perspective?",
    "How can machine learning detect early signs of dangerous diseases before symptoms appear, potentially increasing survival rates for millions of patients?",
    "What is the meaning of life?","What is consciousness?","What is the nature of reality?","What is free will?","What is the mind-body problem?","What is the self?",
    "What is time?","What is space?","What is truth?","What is beauty?","What is justice?",
    "What is morality?","What is knowledge?","What is existence?","What is love?","What is happiness?","What is death?",
    "What is the universe?","What is infinity?","What is identity?","What is art?","What is science?",
    "What is religion?","What is culture?","What is society?","What is language?","What is power?",
    "What is freedom?","What is equality?","What is diversity?","What is creativity?","What is innovation?",
    "What is intelligence and can it be accurately measured by IQ tests?",
    "How does social media influence mental health, self-esteem, and human relationships over long periods of time?",
    "What is the impact of artificial intelligence on future job markets and human creativity?",
    "How do habits form in the brain and what is the most effective way to change bad habits permanently?",
    "What causes procrastination from a psychological perspective and how can it be overcome effectively?",
    "How does sleep affect learning, memory consolidation, and emotional regulation?",
    "What is the role of education systems in shaping critical thinking versus rote memorization?",
    "How do emotions influence logical thinking and decision-making processes in everyday life?",
    "What are the ethical challenges of using big data and surveillance technologies in modern societies?",
    "How does storytelling shape human culture, beliefs, and collective memory across generations?",
    "Can humans ever achieve true happiness, or is happiness always temporary by nature?","Grand Theft Auto V","Red Dead Redemption 2","The Witcher 3","Cyberpunk 2077","Elden Ring","Dark Souls III","Sekiro: Shadows Die Twice",
    "God of War","God of War Ragnarok","Assassin's Creed Valhalla","Assassin's Creed Odyssey","Call of Duty: Modern Warfare",
    "Call of Duty: Warzone","Battlefield 1","Battlefield V","FIFA 23","eFootball","NBA 2K23","Fortnite","Apex Legends","PUBG","Valorant",
    "Counsychological theories explain the phenomenon of cognitive dissonance and how does it affect decision-making processes?",
    "How doter-Strike 2","League of Legends","Dota 2","Overwatch 2","Rocket League","Among Us","Fall Guys","The Legend of Zelda: Breath of the Wild","Minecraft",
    "The Legend of Zelda: Tears of the Kingdom","Super Mario Odyssey","Animal Crossing: New Horizons","Resident Evil 4",
    "Resident Evil Village","Silent Hill 2","Horizon Zero Dawn","Horizon Forbidden West","Death Stranding","Metal Gear Solid V","Uncharted 4","The Last of Us",
    "The Last of Us Part II","Spider-Man Remastered","Spider-Man: Miles Morales","Bloodborne","Monster Hunter World","Skyrim","Fallout 4","Starfield",
    "No Man's Sky","Far Cry 5","Far Cry 6","Watch Dogs 2","Ghost of Tsushima","Tomb Raider","Rise of the Tomb Raider","Shadow of the Tomb Raider","Diablo IV"
]

def get_wait_time(condition):
    modes = {
        "fast": (8, 12),
        "normal": (60, 120),
        "slow": (300, 600)
    }
    return random.uniform(*modes.get(condition, modes["normal"]))

def pc_auto_search(condition="normal",update_progress=None):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-notifications")
    temp_dir = tempfile.mkdtemp()
    options.add_argument(f"user-data-dir={temp_dir}")
    driver = webdriver.Edge(options=options)
    driver.get("https://rewards.bing.com/")
    questions = random.sample(SEARCH_LIST, k=min(len(SEARCH_LIST), 31))
    total = len(questions)
    try:
        time.sleep(3)
        for i, q in enumerate(questions, 1):
            driver.get(f"https://www.bing.com/search?q={q}")
            print(f"[PC {i}] {q}")
            if update_progress:
                update_progress()
            time.sleep(get_wait_time(condition))
    finally:
        driver.quit()

def mobile_auto_search(condition="normal",update_progress=None):
    options = Options()
    options.add_experimental_option(
        "mobileEmulation", {"deviceName": "iPhone X"}
    )
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    temp_dir = tempfile.mkdtemp()
    options.add_argument(f"user-data-dir={temp_dir}")
    driver = webdriver.Edge(options=options)
    driver.get("https://rewards.bing.com/")
    questions = random.sample(SEARCH_LIST, k=min(len(SEARCH_LIST), 21))
    try:
        time.sleep(3)
        for i, q in enumerate(questions, 1):
            driver.get(f"https://www.bing.com/search?q={q}")
            print(f"[Mobile {i}] {q}")
            if update_progress:
                update_progress()
            time.sleep(get_wait_time(condition))
    finally:
        driver.quit()

def pc_mobile_auto_search(condition="normal"):
    t1 = threading.Thread(target=pc_auto_search, args=(condition,))
    t2 = threading.Thread(target=mobile_auto_search, args=(condition,))
    t1.start()
    time.sleep(3)
    t2.start()
    t1.join()
    t2.join()

def start_search():
    mode = search_type.get()
    speed = speed_choice.get()
    if mode == -1:
        messagebox.showwarning("Warning", "Please choose search type")
        return
    status_text.set(f"Running ({speed})...")
    start_btn.config(state="disabled")
    if mode == 0:
        total_steps = 31
    elif mode == 1:
        total_steps = 21
    else:
        total_steps = 52
    progress["maximum"] = total_steps
    progress_var.set(0)

    current_step.set(0)
    total_steps_var.set(total_steps)
    progress_label.config(text=f"0 / {total_steps}")
    progress_var.set(0)
    def update_progress():
        def _update():
            current_step.set(current_step.get() + 1)
            progress_var.set(current_step.get())
            progress_label.config(text=f"{current_step.get()} / {total_steps_var.get()}")
        root.after(0, _update)

    def run():
        try:
            if mode == 0:
                pc_auto_search(speed, update_progress)
            elif mode == 1:
                mobile_auto_search(speed, update_progress)
            elif mode == 2:
                t1 = threading.Thread(
                    target=pc_auto_search, args=(speed, update_progress)
                )
                t2 = threading.Thread(
                    target=mobile_auto_search, args=(speed, update_progress)
                )
                t1.start()
                t2.start()
                t1.join()
                t2.join()
        finally:
            root.after(0, lambda: status_text.set("Ready"))
            root.after(0, lambda: start_btn.config(state="normal"))
            root.after(0, lambda: search_type.set(-1))
            root.after(0, lambda: progress_var.set(0))
            root.after(0, lambda: progress_label.config(text="0 / 0"))
    threading.Thread(target=run, daemon=True).start()

# main window
root = tk.Tk()
root.title("Bing Auto Search")
root.geometry("460x340+800+320")
root.resizable(False, False)
search_type = tk.IntVar(value=-1)
speed_choice = tk.StringVar(value="normal")
status_text = tk.StringVar(value="Ready")
# search types 
tk.Label(root, text="Choose Search Type", font=("Arial", 10, "bold")).pack(pady=10)
tk.Radiobutton(root, text="PC Search", variable=search_type, value=0).pack()
tk.Radiobutton(root, text="Mobile Search", variable=search_type, value=1).pack()
tk.Radiobutton(root, text="PC and Mobile Search", variable=search_type, value=2).pack()
# speed types
tk.Label(root, text="Choose Speed", font=("Arial", 10, "bold")).pack(pady=10)
speed_frame = tk.Frame(root)
speed_frame.pack(pady=5)
tk.Radiobutton(speed_frame,text="Fast (not recommended)\n 8-12sec",variable=speed_choice,value="fast").pack(side="left", padx=15)
tk.Radiobutton(speed_frame,text="Normal\n 1-2min",variable=speed_choice,value="normal").pack(side="left", padx=15)
tk.Radiobutton(speed_frame,text="Slow (recommended)\n 5 -10min",variable=speed_choice,value="slow").pack(side="left", padx=15)
tk.Label(root, textvariable=status_text, fg="blue").pack(pady=5)
# start button
start_btn = tk.Button(root, text="Start", width=15,bg="green", fg="white",command=start_search)
start_btn.pack()
# progress bar
current_step = tk.IntVar(value=0)
total_steps_var = tk.IntVar(value=0)
progress_label = tk.Label(root,text="0 / 0",font=("Arial", 9, "bold"))
progress_label.pack(pady=(5, 0))
progress_var = tk.IntVar(value=0)
progress = ttk.Progressbar(root,orient="horizontal",length=300,mode="determinate",variable=progress_var)
progress.pack(pady=5)
root.mainloop()
# made by bot0xic
