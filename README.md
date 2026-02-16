# 🎬 Zero Touch Shorts  

**Zero Touch Shorts** is a fully automated platform designed to generate, render, and upload **YouTube Shorts videos** with fascinating random facts — all with zero manual intervention. Using AI-powered automation, scheduling, and workflow orchestration, it allows creators and channels to maintain a consistent presence effortlessly.  

Whether you are a solo content creator, a YouTube channel owner, or a developer exploring automated content creation, Zero Touch Shorts handles the **entire video pipeline end-to-end**.  

---

# 🚀 Overview  

Zero Touch Shorts automates the full content creation and publishing process:

### 1. Fact Fetching & Audio Generation
- Fetches unique random facts from a public API.  
- Converts facts into natural speech using **Google Text-to-Speech**.  

### 2. Video Production
- Automatically generates cinematic 50–60 second vertical Shorts.  
- Features include:  
  - 3-second attention-grabbing hook  
  - Karaoke-style word-by-word text synced to audio  
  - Animated Ken Burns effect with cross-dissolve transitions  
  - Floating particles, progress bars, intro/outro cards, and subscribe popups  
  - Ambient background music  
- Automatically generates custom thumbnails.  

### 3. YouTube Upload
- Uploads videos via the **YouTube Data API**.  
- Automatically populates optimized metadata:  
  - Titles  
  - Descriptions  
  - 30 rotating hashtags  
  - Pinned engagement comments  
  - Playlist assignment  
- Ensures better discoverability and SEO optimization.  

### 4. Scheduling & Automation
- Fully zero-touch publishing at predefined intervals.  
- Default scheduling: 10 videos/day between 12 PM–11 PM EST.  

### 5. Notifications
- Optional email notifications for uploads and system events.  
- Default contact email: `zerotouchai.official@gmail.com`.  

---

# ✨ Key Features  

- ✅ **End-to-End Automation** – From fact fetching to YouTube upload.  
- ✅ **Cinematic Shorts** – Engaging videos with professional animation and audio.  
- ✅ **SEO Optimization** – Titles, descriptions, hashtags, and pinned comments automatically managed.  
- ✅ **Custom Thumbnails** – Automatically generated for each video.  
- ✅ **Persistent Fact Tracking** – Prevents repeating facts using `used_facts.json`.  
- ✅ **Scalable & Efficient** – Ideal for creators, educational channels, or content automation projects.  

---

# 🛠 Requirements  

- Python 3.9+  
- Google OAuth credentials for YouTube Data API v3  
- Unsplash API key for background images  
- FFmpeg installed and added to system PATH  
- Internet connection for API and uploads  

---

# ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zerotouchaiofficial/zero-touch-shorts.git
cd zero-touch-shorts
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Secrets

* Google OAuth credentials (for YouTube API)
* Unsplash API key
* Add both as GitHub Secrets for secure workflow automation.
  ⚠️ Never commit secrets or API keys to the repository. Use GitHub Secrets or `.env` files.

### 5️⃣ Run the Automation

* The workflow runs automatically on GitHub Actions.
* To test locally:

```bash
python main.py
```

---

## 📂 Configuration Options

### 🎥 Video Settings

* Resolution: 1080x1920 (vertical Shorts)
* Frame rate: 30fps
* Background animation: Ken Burns effect + floating particles
* Intro/outro cards and subscribe popup

### 📝 Metadata Settings

* Title template
* Description template
* 30 rotating hashtags
* Playlist assignment
* Pinned engagement comment

### ⏱ Scheduler

* Number of videos per day
* Start/end time (timezone configurable)

### 📧 Notifications

* Optional email alerts for successful uploads or errors
* Default: `zerotouchai.official@gmail.com`

---

## 🤝 Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for:

* Branching & pull request guidelines
* Coding standards
* Reporting bugs or requesting features

Whether it’s adding new features, fixing bugs, or improving documentation, your contributions are appreciated.

---

## 🛡 Security

* Follow `SECURITY.md` for reporting vulnerabilities responsibly.
* Never expose API credentials or sensitive information.
* Do not create public issues for security concerns.

---

## 📜 Code of Conduct

We follow `CODE_OF_CONDUCT.md` to maintain a safe and inclusive community. Key points:

* Be respectful and constructive in communication
* Avoid harassment, discrimination, or offensive behavior
* Report violations responsibly

---

## 📌 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## ⚠️ Disclaimer

* Provided as-is without warranties.
* You are responsible for ensuring compliance with YouTube Terms of Service.
* Safeguard API credentials and account security.
* The maintainers are not responsible for misuse or account penalties.

---

## 📧 Contact

For questions, support, or collaborations:

* Email: `zerotouchai.official@gmail.com`

🚀 **Create once. Automate forever.**
