# Linguini Game - Audio Generation System

Complete system for generating language audio files using Google Cloud Text-to-Speech

## 📁 Files Included

1. **generate_tts_audio.py** - Main script to generate all audio files
2. **test_tts.py** - Test script to verify setup
3. **SETUP_GUIDE.md** - Detailed setup instructions
4. **game_integration_example.js** - How to use the audio in your game

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install google-cloud-texttospeech
```

### 2. Set Up Google Cloud (5 minutes)
- Create account at https://cloud.google.com/ (free $300 credit!)
- Enable Cloud Text-to-Speech API
- Create service account credentials
- Download JSON key file

See **SETUP_GUIDE.md** for detailed steps.

### 3. Set Credentials
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-credentials.json"
```

### 4. Test Your Setup
```bash
python test_tts.py
```

This creates one test audio file. If it works, proceed!

### 5. Generate All Audio Files
```bash
python generate_tts_audio.py
```

This will:
- Generate ~200 MP3 files (50 languages × 2 phrases × 2 genders)
- Create `language_data.json` with all metadata
- Take about 5-10 minutes to complete

## 📊 What You'll Get

### Directory Structure
```
audio_files/
├── Spanish_male_phrase1.mp3
├── Spanish_female_phrase1.mp3
├── Spanish_male_phrase2.mp3
├── Spanish_female_phrase2.mp3
├── French_male_phrase1.mp3
├── French_female_phrase1.mp3
├── ... (200 files total)
└── ...

language_data.json  (metadata)
```

### Language Data JSON Example
```json
[
  {
    "name": "Spanish",
    "code": "es-ES",
    "location": [40.4168, -3.7038],
    "audio_files": [
      {
        "filename": "Spanish_male_phrase1.mp3",
        "phrase_number": 1,
        "gender": "male",
        "text": "Welcome to our beautiful country..."
      },
      ...
    ]
  },
  ...
]
```

## 🌍 Languages Included (Top 50)

1. Mandarin Chinese
2. Spanish
3. English
4. Hindi
5. Bengali
6. Portuguese
7. Russian
8. Japanese
9. Punjabi
10. German
11. Javanese
12. Malay
13. Telugu
14. Vietnamese
15. Korean
16. French
17. Marathi
18. Tamil
19. Turkish
20. Urdu
21. Gujarati
22. Polish
23. Ukrainian
24. Kannada
25. Malayalam
26. Italian
27. Sundanese
28. Romanian
29. Thai
30. Dutch
31. Greek
32. Czech
33. Swedish
34. Hungarian
35. Azerbaijani*
36. Hausa*
37. Persian*
38. Swahili
39. Arabic
40. Burmese*
41. Uzbek*
42. Amharic*
43. Tagalog
44. Yoruba*
45. Malagasy*
46. Nepali
47. Sinhala
48. Khmer
49-50. (Additional languages)

*Limited voice support - may use similar language as fallback

## 💰 Cost

**FREE for your prototype!**

- Google Cloud gives you:
  - $300 free credit for 90 days
  - 1 million characters/month FREE forever
- This script uses ~50,000 characters
- You're well within free limits!

Even if you exceed free tier later:
- $4 per million characters (Standard)
- For reference: 1 million chars ≈ 20,000 phrases

## 🎮 Integration with Your Game

See `game_integration_example.js` for complete examples.

### Basic Usage
```javascript
// Load language data
const languages = await fetch('language_data.json').then(r => r.json());

// Select today's language
const today = languages[0]; // or use date-based selection

// Play audio
const audio = new Audio(`audio_files/${today.audio_files[0].filename}`);
audio.play();
```

### Daily Challenge Pattern
```javascript
// Use date as seed for consistent daily puzzle
function selectDailyLanguage(languages) {
    const dateString = new Date().toISOString().split('T')[0];
    const seed = parseInt(dateString.replace(/-/g, ''));
    return languages[seed % languages.length];
}
```

## 🎯 Features

✅ **50 languages** - Top languages by number of speakers
✅ **2 genders** - Male and female voices for each language
✅ **2 phrases** - Variety to prevent memorization
✅ **Natural voices** - Google's neural TTS sounds human-like
✅ **Geographic data** - Lat/lng coordinates for each language
✅ **Metadata** - JSON file with all information
✅ **Free** - Well within Google's free tier

## 🔧 Customization

Want to change the phrases? Edit this section in `generate_tts_audio.py`:

```python
phrases = [
    "Your first phrase here...",
    "Your second phrase here..."
]
```

Want different languages? Modify the `languages` list in the script.

Want more variety? Add more phrases to the list!

## 📝 License & Usage

- ✅ Generated audio files are **yours** - no copyright issues
- ✅ Can use **commercially** in your game
- ✅ No attribution required (though crediting Google TTS is nice!)
- ✅ Audio is synthetic, not recordings of real people

## 🆘 Troubleshooting

### "Could not load credentials"
→ Check that `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set

### "API not enabled"
→ Enable Cloud Text-to-Speech API in Google Cloud Console

### "Permission denied"
→ Make sure service account has "Cloud Text-to-Speech User" role

### Some languages fail
→ Normal! Not all 50 languages have full TTS support. The script continues with others.

### File size concerns
→ 200 MP3 files ≈ 20-50 MB total. Very manageable!

## 🚀 Next Steps

After generating audio files:

1. **Upload to your web server**
   - Put `audio_files/` folder on your server
   - Put `language_data.json` on your server

2. **Integrate into game**
   - See `game_integration_example.js`
   - Load the JSON data
   - Play audio files based on selected language

3. **Add difficulty modes**
   - Easy: Top 20 languages
   - Medium: Top 35 languages  
   - Hard: All 50 languages

4. **Test thoroughly**
   - Play each language to verify quality
   - Check that locations match languages
   - Ensure audio files load properly

## 🎊 You're All Set!

You now have:
- ✅ 200 professional audio files
- ✅ Complete language metadata
- ✅ Geographic coordinates
- ✅ Integration examples
- ✅ Zero cost (free tier)

Ready to make your game addictive! 🌍🎮

## 📧 Questions?

- Google Cloud TTS Docs: https://cloud.google.com/text-to-speech/docs
- Supported languages: https://cloud.google.com/text-to-speech/docs/voices
- Pricing calculator: https://cloud.google.com/text-to-speech/pricing
