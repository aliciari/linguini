#!/usr/bin/env python3
"""
Google Cloud Text-to-Speech Audio Generator for Linguini Game
Generates audio files in 50 languages with male and female voices
"""

import os
import json
from google.cloud import texttospeech

# OPTION: If environment variable doesn't work, uncomment and edit this line:
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Admin\linguini-audio-generator\linguini-game-263276733d95.json'

# Initialize the Text-to-Speech client
# Note: You need to set up Google Cloud credentials first
# export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-credentials.json"

def generate_audio_files():
    """Generate audio files for all languages"""
    
    client = texttospeech.TextToSpeechClient()
    
    # Top 50 languages by speakers with their Google Cloud language codes
    languages = [
        # Format: (Language Name, Google Language Code, Primary Location [lat, lng])
        ("Mandarin Chinese", "cmn-CN", [39.9042, 116.4074]),  # Beijing
        ("Spanish", "es-ES", [40.4168, -3.7038]),  # Madrid
        ("English", "en-US", [38.9072, -77.0369]),  # Washington DC
        ("Hindi", "hi-IN", [28.6139, 77.2090]),  # New Delhi
        ("Bengali", "bn-IN", [22.5726, 88.3639]),  # Kolkata
        ("Portuguese", "pt-BR", [-15.7975, -47.8919]),  # Brasilia
        ("Russian", "ru-RU", [55.7558, 37.6173]),  # Moscow
        ("Japanese", "ja-JP", [35.6762, 139.6503]),  # Tokyo
        ("Punjabi", "pa-IN", [30.7333, 76.7794]),  # Chandigarh
        ("German", "de-DE", [52.5200, 13.4050]),  # Berlin
        ("Javanese", "jv-ID", [-7.7956, 110.3695]),  # Yogyakarta
        ("Wu Chinese", "cmn-CN", [31.2304, 121.4737]),  # Shanghai (using Mandarin)
        ("Malay", "ms-MY", [3.1390, 101.6869]),  # Kuala Lumpur
        ("Telugu", "te-IN", [17.3850, 78.4867]),  # Hyderabad
        ("Vietnamese", "vi-VN", [21.0285, 105.8542]),  # Hanoi
        ("Korean", "ko-KR", [37.5665, 126.9780]),  # Seoul
        ("French", "fr-FR", [48.8566, 2.3522]),  # Paris
        ("Marathi", "mr-IN", [19.0760, 72.8777]),  # Mumbai
        ("Tamil", "ta-IN", [13.0827, 80.2707]),  # Chennai
        ("Turkish", "tr-TR", [39.9334, 32.8597]),  # Ankara
        ("Urdu", "ur-IN", [28.6139, 77.2090]),  # New Delhi
        ("Gujarati", "gu-IN", [23.0225, 72.5714]),  # Ahmedabad
        ("Polish", "pl-PL", [52.2297, 21.0122]),  # Warsaw
        ("Ukrainian", "uk-UA", [50.4501, 30.5234]),  # Kyiv
        ("Kannada", "kn-IN", [12.9716, 77.5946]),  # Bangalore
        ("Malayalam", "ml-IN", [8.5241, 76.9366]),  # Trivandrum
        ("Oriya", "or-IN", [20.2961, 85.8245]),  # Bhubaneswar (limited support)
        ("Italian", "it-IT", [41.9028, 12.4964]),  # Rome
        ("Sundanese", "su-ID", [-6.9175, 107.6191]),  # Bandung
        ("Romanian", "ro-RO", [44.4268, 26.1025]),  # Bucharest
        ("Thai", "th-TH", [13.7563, 100.5018]),  # Bangkok
        ("Dutch", "nl-NL", [52.3676, 4.9041]),  # Amsterdam
        ("Greek", "el-GR", [37.9838, 23.7275]),  # Athens
        ("Czech", "cs-CZ", [50.0755, 14.4378]),  # Prague
        ("Swedish", "sv-SE", [59.3293, 18.0686]),  # Stockholm
        ("Hungarian", "hu-HU", [47.4979, 19.0402]),  # Budapest
        ("Azerbaijani", "az-AZ", [40.4093, 49.8671]),  # Baku (limited support)
        ("Hausa", "ha-NG", [9.0765, 7.3986]),  # Abuja (limited support)
        ("Persian", "fa-IR", [35.6892, 51.3890]),  # Tehran (limited support)
        ("Swahili", "sw-KE", [-1.2864, 36.8172]),  # Nairobi
        ("Arabic", "ar-XA", [24.7136, 46.6753]),  # Riyadh
        ("Burmese", "my-MM", [16.8661, 96.1951]),  # Yangon (limited support)
        ("Uzbek", "uz-UZ", [41.2995, 69.2401]),  # Tashkent (limited support)
        ("Amharic", "am-ET", [9.0320, 38.7469]),  # Addis Ababa (limited support)
        ("Tagalog", "fil-PH", [14.5995, 120.9842]),  # Manila
        ("Yoruba", "yo-NG", [7.3775, 3.9470]),  # Lagos (limited support)
        ("Malagasy", "mg-MG", [-18.8792, 47.5079]),  # Antananarivo (limited support)
        ("Nepali", "ne-NP", [27.7172, 85.3240]),  # Kathmandu
        ("Sinhala", "si-LK", [6.9271, 79.8612]),  # Colombo
        ("Khmer", "km-KH", [11.5564, 104.9282]),  # Phnom Penh
    ]
    
    # Phrases in each language - we'll use simple, common phrases
    # For each language, we'll define appropriate text in that language
    language_phrases = {
        "cmn-CN": ["欢迎来到我们美丽的国家，这里古老的传统与现代生活相遇。", "今天天气很好，人们正在外面享受时光。"],
        "es-ES": ["Bienvenido a nuestro hermoso país, donde las tradiciones antiguas se encuentran con la vida moderna.", "El clima es encantador hoy, y la gente está disfrutando su tiempo afuera."],
        "en-US": ["Welcome to our beautiful country, where ancient traditions meet modern life.", "The weather is lovely today, and people are enjoying their time outside."],
        "hi-IN": ["हमारे सुंदर देश में आपका स्वागत है, जहां प्राचीन परंपराएं आधुनिक जीवन से मिलती हैं।", "आज मौसम सुहावना है, और लोग बाहर अपना समय बिता रहे हैं।"],
        "bn-IN": ["আমাদের সুন্দর দেশে স্বাগতম, যেখানে প্রাচীন ঐতিহ্য আধুনিক জীবনের সাথে মিলিত হয়।", "আজ আবহাওয়া সুন্দর, এবং মানুষ বাইরে তাদের সময় উপভোগ করছে।"],
        "pt-BR": ["Bem-vindo ao nosso lindo país, onde tradições antigas encontram a vida moderna.", "O clima está lindo hoje, e as pessoas estão aproveitando o tempo lá fora."],
        "ru-RU": ["Добро пожаловать в нашу прекрасную страну, где древние традиции встречаются с современной жизнью.", "Сегодня прекрасная погода, и люди наслаждаются временем на улице."],
        "ja-JP": ["古い伝統と現代生活が出会う美しい国へようこそ。", "今日は天気が良く、人々は外で時間を楽しんでいます。"],
        "pa-IN": ["ਸਾਡੇ ਸੁੰਦਰ ਦੇਸ਼ ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ, ਜਿੱਥੇ ਪ੍ਰਾਚੀਨ ਪਰੰਪਰਾਵਾਂ ਆਧੁਨਿਕ ਜੀਵਨ ਨਾਲ ਮਿਲਦੀਆਂ ਹਨ।", "ਅੱਜ ਮੌਸਮ ਬਹੁਤ ਵਧੀਆ ਹੈ, ਅਤੇ ਲੋਕ ਬਾਹਰ ਆਪਣਾ ਸਮਾਂ ਮਾਣ ਰਹੇ ਹਨ।"],
        "de-DE": ["Willkommen in unserem schönen Land, wo alte Traditionen auf modernes Leben treffen.", "Das Wetter ist heute herrlich, und die Leute genießen ihre Zeit draußen."],
        "ms-MY": ["Selamat datang ke negara kami yang indah, di mana tradisi purba bertemu dengan kehidupan moden.", "Cuaca hari ini sangat menyenangkan, dan orang ramai menikmati masa mereka di luar."],
        "te-IN": ["మా అందమైన దేశానికి స్వాగతం, ఇక్కడ పురాతన సంప్రదాయాలు ఆధునిక జీవితంతో కలుస్తాయి।", "ఈరోజు వాతావరణం చాలా బాగుంది, మరియు ప్రజలు బయట తమ సమయాన్ని ఆనందిస్తున్నారు।"],
        "vi-VN": ["Chào mừng đến với đất nước xinh đẹp của chúng tôi, nơi truyền thống cổ xưa gặp gỡ cuộc sống hiện đại.", "Thời tiết hôm nay thật đẹp, và mọi người đang tận hưởng thời gian bên ngoài."],
        "ko-KR": ["고대 전통과 현대 생활이 만나는 아름다운 우리나라에 오신 것을 환영합니다.", "오늘 날씨가 좋아서 사람들이 밖에서 시간을 즐기고 있습니다."],
        "fr-FR": ["Bienvenue dans notre beau pays, où les traditions anciennes rencontrent la vie moderne.", "Le temps est magnifique aujourd'hui, et les gens profitent de leur temps dehors."],
        "mr-IN": ["आमच्या सुंदर देशात आपले स्वागत आहे, जिथे प्राचीन परंपरा आधुनिक जीवनाशी भेटतात.", "आज हवामान खूप छान आहे, आणि लोक बाहेर त्यांचा वेळ घालवत आहेत."],
        "ta-IN": ["பழமையான பாரம்பரியங்கள் நவீன வாழ்க்கையை சந்திக்கும் எங்கள் அழகான நாட்டிற்கு வரவேற்கிறோம்.", "இன்று வானிலை மிகவும் இனிமையானது, மக்கள் வெளியில் தங்கள் நேரத்தை அனுபவித்து வருகின்றனர்."],
        "tr-TR": ["Eski geleneklerin modern hayatla buluştuğu güzel ülkemize hoş geldiniz.", "Bugün hava çok güzel ve insanlar dışarıda vakit geçiriyor."],
        "ur-IN": ["ہمارے خوبصورت ملک میں خوش آمدید، جہاں قدیم روایات جدید زندگی سے ملتی ہیں۔", "آج موسم بہت خوشگوار ہے، اور لوگ باہر اپنا وقت گزار رہے ہیں۔"],
        "gu-IN": ["અમારા સુંદર દેશમાં આપનું સ્વાગત છે, જ્યાં પ્રાચીન પરંપરાઓ આધુનિક જીવન સાથે મળે છે.", "આજે હવામાન ખૂબ સરસ છે, અને લોકો બહાર તેમનો સમય માણી રહ્યા છે."],
        "pl-PL": ["Witamy w naszym pięknym kraju, gdzie starożytne tradycje spotykają się z nowoczesnym życiem.", "Dziś pogoda jest cudowna, a ludzie cieszą się czasem na zewnątrz."],
        "uk-UA": ["Ласкаво просимо до нашої прекрасної країни, де давні традиції зустрічаються з сучасним життям.", "Сьогодні чудова погода, і люди насолоджуються часом на вулиці."],
        "kn-IN": ["ಪ್ರಾಚೀನ ಸಂಪ್ರದಾಯಗಳು ಆಧುನಿಕ ಜೀವನವನ್ನು ಭೇಟಿಯಾಗುವ ನಮ್ಮ ಸುಂದರ ದೇಶಕ್ಕೆ ಸುಸ್ವಾಗತ.", "ಇಂದು ಹವಾಮಾನ ತುಂಬಾ ಚೆನ್ನಾಗಿದೆ, ಮತ್ತು ಜನರು ಹೊರಗೆ ತಮ್ಮ ಸಮಯವನ್ನು ಆನಂದಿಸುತ್ತಿದ್ದಾರೆ."],
        "ml-IN": ["പുരാതന പാരമ്പര്യങ്ങൾ ആധുനിക ജീവിതവുമായി കണ്ടുമുട്ടുന്ന ഞങ്ങളുടെ മനോഹരമായ രാജ്യത്തേക്ക് സ്വാഗതം.", "ഇന്ന് കാലാവസ്ഥ വളരെ മനോഹരമാണ്, ആളുകൾ പുറത്ത് സമയം ആസ്വദിക്കുന്നു."],
        "it-IT": ["Benvenuti nel nostro bellissimo paese, dove le antiche tradizioni incontrano la vita moderna.", "Il tempo è incantevole oggi, e la gente si sta godendo il tempo all'aperto."],
        "ro-RO": ["Bine ați venit în frumoasa noastră țară, unde tradițiile antice se întâlnesc cu viața modernă.", "Vremea este minunată astăzi, iar oamenii se bucură de timpul petrecut afară."],
        "th-TH": ["ยินดีต้อนรับสู่ประเทศที่สวยงามของเรา ที่ซึ่งประเพณีโบราณพบกับชีวิตสมัยใหม่", "วันนี้อากาศดีมาก และผู้คนกำลังเพลิดเพลินกับเวลาข้างนอก"],
        "nl-NL": ["Welkom in ons prachtige land, waar oude tradities samenkomen met het moderne leven.", "Het weer is heerlijk vandaag, en mensen genieten van hun tijd buiten."],
        "el-GR": ["Καλώς ήρθατε στην όμορφη χώρα μας, όπου οι αρχαίες παραδόσεις συναντούν τη σύγχρονη ζωή.", "Ο καιρός είναι υπέροχος σήμερα και οι άνθρωποι απολαμβάνουν τον χρόνο τους έξω."],
        "cs-CZ": ["Vítejte v naší krásné zemi, kde se starověké tradice setkávají s moderním životem.", "Počasí je dnes nádherné a lidé si užívají čas venku."],
        "sv-SE": ["Välkommen till vårt vackra land, där gamla traditioner möter modernt liv.", "Vädret är härligt idag, och människor njuter av sin tid utomhus."],
        "hu-HU": ["Üdvözöljük gyönyörű országunkban, ahol az ősi hagyományok találkoznak a modern élettel.", "Ma csodálatos az idő, és az emberek élvezik az időt a szabadban."],
        "sw-KE": ["Karibu nchi yetu nzuri, ambapo mila za kale zinakutana na maisha ya kisasa.", "Hali ya hewa ni nzuri leo, na watu wanafurahia muda wao nje."],
        "ar-XA": ["مرحباً بكم في بلدنا الجميل، حيث تلتقي التقاليد القديمة بالحياة الحديثة.", "الطقس جميل اليوم، والناس يستمتعون بوقتهم في الخارج."],
        "fil-PH": ["Maligayang pagdating sa aming magandang bansa, kung saan nagsasama ang sinaunang tradisyon at modernong buhay.", "Ang panahon ay napakaganda ngayon, at ang mga tao ay nag-eenjoy ng kanilang oras sa labas."],
        "am-ET": ["ወደ ውብ አገራችን እንኳን ደህና መጡ፣ የጥንት ባህሎች ዘመናዊ ህይወትን የሚያገናኙበት።", "ዛሬ የአየር ሁኔታ በጣም ቆንጆ ነው፣ እና ሰዎች ውጭ ጊዜያቸውን እያደረጉ ነው።"],
        "or-IN": ["ଆମର ସୁନ୍ଦର ଦେଶକୁ ସ୍ୱାଗତ, ଯେଉଁଠାରେ ପ୍ରାଚୀନ ପରମ୍ପରା ଆଧୁନିକ ଜୀବନ ସହିତ ମିଳିତ ହୁଏ।", "ଆଜି ପାଗ ବହୁତ ସୁନ୍ଦର ଅଛି, ଏବଂ ଲୋକମାନେ ବାହାରେ ସେମାନଙ୍କ ସମୟ ଉପଭୋଗ କରୁଛନ୍ତି।"]
    }
    
    # Create output directory
    os.makedirs("audio_files", exist_ok=True)
    
    # Track generation stats
    successful = []
    failed = []
    language_data = []
    
    for lang_name, lang_code, location in languages:
        print(f"\n{'='*60}")
        print(f"Processing: {lang_name} ({lang_code})")
        print(f"{'='*60}")
        
        lang_info = {
            "name": lang_name,
            "code": lang_code,
            "location": location,
            "audio_files": []
        }
        
        # Try to get available voices for this language
        try:
            voices_request = texttospeech.ListVoicesRequest(language_code=lang_code)
            voices_response = client.list_voices(request=voices_request)
            available_voices = voices_response.voices
            
            if not available_voices:
                print(f"⚠️  No voices available for {lang_name} ({lang_code})")
                failed.append(lang_name)
                continue
            
            # Separate male and female voices, prefer Standard/Wavenet voices
            # Filter out voices that require model specification (like Journey voices)
            standard_voices = [v for v in available_voices if 'Standard' in v.name or 'Wavenet' in v.name or 'Neural' in v.name]
            
            # If no standard voices, use all available
            if not standard_voices:
                standard_voices = available_voices
            
            male_voices = [v for v in standard_voices if v.ssml_gender == texttospeech.SsmlVoiceGender.MALE]
            female_voices = [v for v in standard_voices if v.ssml_gender == texttospeech.SsmlVoiceGender.FEMALE]
            
            # Use first available of each gender, or any voice if specific gender not available
            male_voice = male_voices[0] if male_voices else standard_voices[0]
            female_voice = female_voices[0] if female_voices else standard_voices[-1]
            
            print(f"✓ Male voice: {male_voice.name}")
            print(f"✓ Female voice: {female_voice.name}")
            
            # Get phrases for this language, or use English as fallback
            phrases = language_phrases.get(lang_code, language_phrases["en-US"])
            
            # Generate audio for each phrase with each voice
            for phrase_idx, phrase in enumerate(phrases):
                for voice, gender in [(male_voice, "male"), (female_voice, "female")]:
                    try:
                        # Set up the synthesis input
                        synthesis_input = texttospeech.SynthesisInput(text=phrase)
                        
                        # Build the voice request
                        voice_params = texttospeech.VoiceSelectionParams(
                            language_code=lang_code,
                            name=voice.name
                        )
                        
                        # Add model if the voice requires it (Journey voices need this)
                        # We'll use a try-catch to handle this gracefully
                        if 'journey' in voice.name.lower():
                            continue  # Skip journey voices as they need special handling
                        
                        # Select the audio format
                        audio_config = texttospeech.AudioConfig(
                            audio_encoding=texttospeech.AudioEncoding.MP3,
                            speaking_rate=1.0,
                            pitch=0.0
                        )
                        
                        # Perform the text-to-speech request
                        response = client.synthesize_speech(
                            input=synthesis_input,
                            voice=voice_params,
                            audio_config=audio_config
                        )
                        
                        # Create safe filename
                        safe_lang_name = lang_name.replace(" ", "_").replace("/", "_")
                        filename = f"{safe_lang_name}_{gender}_phrase{phrase_idx + 1}.mp3"
                        filepath = os.path.join("audio_files", filename)
                        
                        # Write the response to an MP3 file
                        with open(filepath, "wb") as out:
                            out.write(response.audio_content)
                        
                        print(f"  ✓ Generated: {filename}")
                        
                        lang_info["audio_files"].append({
                            "filename": filename,
                            "phrase_number": phrase_idx + 1,
                            "gender": gender,
                            "text": phrase
                        })
                        
                    except Exception as e:
                        print(f"  ✗ Error generating {gender} phrase {phrase_idx + 1}: {str(e)}")
            
            successful.append(lang_name)
            language_data.append(lang_info)
            
        except Exception as e:
            print(f"✗ Error processing {lang_name}: {str(e)}")
            failed.append(lang_name)
    
    # Save language data to JSON for easy loading in the game
    with open("language_data.json", "w", encoding="utf-8") as f:
        json.dump(language_data, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("\n" + "="*60)
    print("GENERATION SUMMARY")
    print("="*60)
    print(f"✓ Successfully generated: {len(successful)} languages")
    print(f"✗ Failed: {len(failed)} languages")
    
    if failed:
        print(f"\nFailed languages: {', '.join(failed)}")
    
    print(f"\nTotal audio files created: {sum(len(lang['audio_files']) for lang in language_data)}")
    print(f"Language data saved to: language_data.json")
    print(f"Audio files saved to: audio_files/")
    
    # Calculate approximate character usage
    total_chars = len(successful) * sum(len(p) for p in phrases) * 2  # 2 voices per phrase
    print(f"\nApproximate characters used: {total_chars:,}")
    print(f"Well within Google's free tier of 1,000,000 chars/month!")

if __name__ == "__main__":
    print("Google Cloud Text-to-Speech Audio Generator")
    print("=" * 60)
    print("\nIMPORTANT: Before running this script:")
    print("1. Install: pip install google-cloud-texttospeech")
    print("2. Set up Google Cloud credentials:")
    print("   export GOOGLE_APPLICATION_CREDENTIALS='path/to/credentials.json'")
    print("3. Enable the Cloud Text-to-Speech API in your Google Cloud Console")
    print("\nStarting generation...\n")
    
    try:
        generate_audio_files()
    except Exception as e:
        print(f"\n✗ Fatal error: {str(e)}")
        print("\nMake sure you've set up Google Cloud credentials correctly!")