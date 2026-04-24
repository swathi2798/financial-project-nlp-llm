**Objective**

The goal of this project is to build an end-to-end **Financial News Event Extractor** using Natural Language Processing (NLP). The system automatically ingests financial news from multiple sources, processes and classifies key market-moving events, extracts critical entities, scores sentiment, and delivers structured, actionable intelligence to downstream systems and users in real time.

The pipeline follows a modular architecture:

> 📡 Ingestion → ⚙️ Preprocessing → 🧠 NLP Engine → 💾 Storage → 📤 Output
> 

**📊 Results It Will Provide**

- **Real-time alerts** via Telegram, Email, and Slack whenever a high-impact financial event is detected
- **Event classification** across categories: Earnings Announcements, M&A activity, Executive Changes, Lawsuits/Regulatory Actions, Product Launches, Guidance Changes, and Dividend Announcements
- **Entity extraction** — company names mapped to tickers, executives, monetary amounts, dates, and locations
- **Sentiment & impact scoring** — polarity (positive/negative), magnitude (Low → Medium → High), and confidence score (0–100%)
- **Temporal intelligence** — event date, effective date, and filing deadline tracking
- **Dashboard** showing an event timeline per ticker for visual analysis
- **Historical event database** for backtesting and trend analysis
- **API integration** with trading systems for automated decision support

**🛠️ Tools & Technologies Learnt**

- **Data Ingestion**: RSS feeds (Reuters, Bloomberg, Yahoo Finance), APIs (NewsAPI, Alpha Vantage, Finnhub), Web scrapers (Financial Times, WSJ)
- **NLP & ML**: Multi-label event classification, Named Entity Recognition (NER), Sentiment analysis models
- **Storage & Indexing**: PostgreSQL (event database), InfluxDB (time-series trends), Elasticsearch (search indexing)
- **Output & Alerting**: Telegram bots, Email notifications, Slack webhooks
- **Data Engineering**: Text cleaning & normalization, ticker extraction & validation, timestamp standardization, multi-source deduplication

**🔍 Overview**

This project bridges the gap between raw financial news and actionable market intelligence. By automating event detection and classification, it eliminates manual news monitoring and enables faster, data-driven decisions. The modular pipeline design makes it extensible — new news sources, event types, or output channels can be plugged in independently, making it a scalable foundation for financial intelligence systems.
