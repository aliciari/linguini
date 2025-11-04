# Google Cloud Text-to-Speech Setup Guide for Linguini

## Step 1: Create Google Cloud Account

1. Go to https://cloud.google.com/
2. Click "Get started for free"
3. Sign up (you get $300 free credit for 90 days!)
4. No credit card charged during free trial

## Step 2: Enable Text-to-Speech API

1. Go to Google Cloud Console: https://console.cloud.google.com/
2. Create a new project (e.g., "Linguini-Game")
3. Go to "APIs & Services" > "Library"
4. Search for "Cloud Text-to-Speech API"
5. Click "Enable"

## Step 3: Create Service Account & Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "Service Account"
3. Name it (e.g., "linguini-tts")
4. Click "Create and Continue"
5. Grant role: "Cloud Text-to-Speech User"
6. Click "Done"
7. Click on the service account you just created
8. Go to "Keys" tab
9. Click "Add Key" > "Create new key"
10. Choose "JSON"
11. Download the JSON file (keep it secret!)

## Step 4: Install Python Dependencies

```bash
pip install google-cloud-texttospeech
```

## Step 5: Set Up Credentials

### On Mac/Linux:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-credentials.json"
```

### On Windows:
```cmd
set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your-credentials.json"
```

Or add to your system environment variables permanently.

## Step 6: Run the Generator Script

```bash
python generate_tts_audio.py
```

This will:
- Generate audio files for 50 languages
- Create both male and female voices
- Generate 2 phrases per language
- Save ~200 MP3 files to `audio_files/` directory
- Create `language_data.json` with all metadata

## Expected Output

```
audio_files/
  ├── Spanish_male_phrase1.mp3
  ├── Spanish_female_phrase1.mp3
  ├── Spanish_male_phrase2.mp3
  ├── Spanish_female_phrase2.mp3
  ├── French_male_phrase1.mp3
  ├── French_female_phrase1.mp3
  └── ... (~200 files)

language_data.json  (metadata for all languages)
```

## Cost Estimate

- **Free Tier**: 1 million characters per month (forever!)
- **This script**: Uses ~50,000 characters
- **You're well within the free tier!** 🎉

Even after free tier:
- $4 per 1 million characters (Standard voices)
- $16 per 1 million characters (WaveNet/Neural voices)

For this project, you'll likely never pay anything.

## Testing Before Full Generation

Run the test script first to make sure everything works:

```bash
python test_tts.py
```

This will generate just 1 audio file to verify your setup.

## Troubleshooting

### Error: "Could not load the default credentials"
- Make sure GOOGLE_APPLICATION_CREDENTIALS is set correctly
- Check that the JSON file path is correct
- Try using absolute path

### Error: "API has not been enabled"
- Go to Google Cloud Console
- Enable "Cloud Text-to-Speech API"
- Wait a few minutes for it to propagate

### Error: "Permission denied"
- Make sure your service account has "Cloud Text-to-Speech User" role
- Check IAM & Admin > IAM in Google Cloud Console

## Alternative: Use the Web Interface

If you don't want to run Python:
1. Go to: https://cloud.google.com/text-to-speech
2. Try the demo on the page
3. You can manually generate and download files
4. Not ideal for 200 files, but good for testing!

## Next Steps After Generation

1. Upload audio files to your web server
2. Update the game code to load from `language_data.json`
3. Play random audio file when user starts game
4. Track which file was played to check the answer

## Important Notes

- **Keep your credentials.json SECRET** - never commit to GitHub!
- Add to .gitignore: `credentials.json`
- The audio files you generate are YOURS - no copyright issues
- You can use them commercially in your game

## Need Help?

- Google Cloud TTS Docs: https://cloud.google.com/text-to-speech/docs
- Pricing: https://cloud.google.com/text-to-speech/pricing
- Supported languages: https://cloud.google.com/text-to-speech/docs/voices
