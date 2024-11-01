# Twitter Bot with LLaMA AI

An intelligent Twitter bot that generates and posts engaging tweets about data engineering using the LLaMA language model.

## Features
- 🤖 Automated tweet generation using LLaMA 2 model
- 🎯 Focused on data engineering topics
- 🔄 Variable outputs with temperature control
- ✍️ Multiple prompt templates for diversity
- ✅ Character limit compliance for Twitter
- 🔄 Automated posting capability

## Prerequisites
- Python 3.8+
- LLaMA 2 model file (7B-chat quantized version)
- Twitter Developer Account with API credentials

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/TwitterBot.git
   cd TwitterBot
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file:
   ```env
   CONSUMER_KEY=your_twitter_consumer_key
   CONSUMER_SECRET=your_twitter_consumer_secret
   ACCESS_TOKEN=your_twitter_access_token
   ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
   ```

4. Download the LLaMA model:
   - Download the LLaMA 2 7B-chat quantized model
   - Place it in a `models` directory
   - Update the model path in `twitter_bot.py`

## Project Structure

## Usage
Run the bot: 
```bash
python twitter_bot.py
```
    

## Configuration
You can modify the following parameters in `twitter_bot.py`:
- `temperature`: Controls output randomness (0.0 to 1.0)
- `max_new_tokens`: Controls response length
- Prompt templates for tweet generation

## Dependencies
- tweepy
- python-dotenv
- langchain
- ctransformers

## Contributing
Feel free to open issues or submit pull requests for improvements.

## License
MIT License

## Disclaimer
Make sure to comply with Twitter's automation rules and rate limits when using this bot.
=======
# TwitterBot
This repo is for a Bot which will help with my X updates
>>>>>>> d3cb1e73e9715776796395bbf01557d6846dca36
