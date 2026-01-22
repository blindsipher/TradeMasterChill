# RL for Dummies: Intraday Trading with Reinforcement Learning 🚀

Welcome to the **easiest way** to learn Reinforcement Learning for intraday trading! This notebook series will take you from complete beginner to advanced practitioner.

## 📚 What's Inside?

This repository contains 5 comprehensive Jupyter notebooks that teach you how to:
- Understand intraday trading data
- Train RL agents (DQN, PPO, SAC) from scratch
- Implement risk management strategies
- Deploy production-ready trading systems

## 🎯 Who Is This For?

- **Beginners**: No prior RL knowledge needed!
- **Traders**: Want to add AI to your toolkit
- **Data Scientists**: Interested in financial applications
- **Students**: Learning RL through practical examples

## 📊 Available Data

We provide **1-minute intraday data** for 5 futures contracts (year 2020):

| Contract | Description | Records |
|----------|-------------|---------|
| MCL-1m | Micro Crude Oil Futures | 351,028 |
| MGC-1m | Micro Gold Futures | 355,250 |
| mes-1m | Micro E-mini S&P 500 | 350,464 |
| ng | Natural Gas Futures | 336,073 |
| si | Silver Futures | 343,233 |

All data is preprocessed with technical indicators and split into train/valid/test sets.

## 📓 Notebook Series

### 1️⃣ Data Exploration and Preparation
**Time**: 15-20 minutes | **Difficulty**: Beginner

Learn about:
- OHLCV (Open, High, Low, Close, Volume) data structure
- Technical indicators (momentum, volatility)
- Data quality and preprocessing
- Visualization techniques

**Key takeaway**: Understanding your data is 50% of the battle!

### 2️⃣ Simple DQN Training
**Time**: 30-45 minutes | **Difficulty**: Beginner

Your first RL agent! Learn:
- What is Reinforcement Learning?
- DQN (Deep Q-Network) algorithm
- Training a trading agent
- Evaluating performance

**Key takeaway**: RL agents learn by trial and error!

### 3️⃣ PPO Training
**Time**: 30-45 minutes | **Difficulty**: Intermediate

Level up with PPO! Learn:
- Policy gradient methods
- Actor-Critic architecture
- Why PPO is more stable than DQN
- Comparing algorithms

**Key takeaway**: PPO is the industry standard for stable RL!

### 4️⃣ SAC Training
**Time**: 30-45 minutes | **Difficulty**: Intermediate

State-of-the-art RL! Learn:
- Maximum Entropy RL
- Automatic exploration tuning
- Twin critics for stability
- SAC vs DQN vs PPO

**Key takeaway**: SAC is production-ready and robust!

### 5️⃣ Advanced Features
**Time**: 45-60 minutes | **Difficulty**: Advanced

Master the full platform! Learn:
- Custom technical indicators
- Risk management (stop-loss, position sizing)
- Reward function engineering
- Hyperparameter tuning
- Multi-contract strategies
- Production deployment

**Key takeaway**: Risk management is NOT optional!

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.9+ required
python --version

# Check if in correct directory
pwd  # Should be in TradeMasterChill/
```

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install TradeMaster
pip install -e .
```

### Running the Notebooks

```bash
# Navigate to notebooks folder
cd rl_intraday_trading_notebooks

# Start Jupyter
jupyter notebook

# Open notebooks in order: 1 → 2 → 3 → 4 → 5
```

## 📁 Folder Structure

```
rl_intraday_trading_notebooks/
├── 1_Data_Exploration_and_Preparation.ipynb
├── 2_Simple_DQN_Training.ipynb
├── 3_PPO_Training.ipynb
├── 4_SAC_Training.ipynb
├── 5_Advanced_Features.ipynb
├── README.md (this file)
├── data/
│   ├── MCL-1m/
│   │   ├── train.csv
│   │   ├── valid.csv
│   │   └── test.csv
│   ├── MGC-1m/
│   ├── mes-1m/
│   ├── ng/
│   ├── si/
│   └── preprocess_data.py
├── configs/
│   ├── config_MCL-1m.py
│   ├── config_MGC-1m.py
│   ├── config_mes-1m.py
│   ├── config_ng.py
│   ├── config_si.py
│   └── create_configs.py
└── saved_models/
    └── (trained models will be saved here)
```

## 🎓 Learning Path

### Week 1: Fundamentals
- Day 1-2: Notebook 1 (Data)
- Day 3-4: Notebook 2 (DQN)
- Day 5: Review and experiment

### Week 2: Advanced Algorithms
- Day 1-2: Notebook 3 (PPO)
- Day 3-4: Notebook 4 (SAC)
- Day 5: Compare algorithms

### Week 3: Production Ready
- Day 1-3: Notebook 5 (Advanced)
- Day 4-5: Build your own strategy

## 🔬 Experimentation Ideas

Once you've completed the notebooks, try:

1. **Different Contracts**: Compare performance across MCL, MGC, mes, ng, si
2. **Hyperparameter Tuning**: Adjust learning rates, batch sizes, network architectures
3. **Custom Indicators**: Add your favorite technical indicators
4. **Risk Management**: Implement different stop-loss strategies
5. **Ensemble Methods**: Combine multiple agents
6. **Market Conditions**: Test on bull/bear markets separately

## 📊 Algorithm Comparison

| Algorithm | Pros | Cons | Best For |
|-----------|------|------|----------|
| **DQN** | Fast, simple, easy to understand | Can be unstable, discrete actions only | Prototyping, learning |
| **PPO** | Stable, general-purpose, proven | Slower than DQN | Consistent performance |
| **SAC** | State-of-the-art, auto-tuning, robust | More complex | Production systems |

## ⚠️ Important Disclaimers

### Trading Risks
- **This is educational material only**
- **Not financial advice**
- **Trading involves substantial risk of loss**
- **Past performance ≠ future results**
- **Always paper trade before live trading**

### Realistic Expectations
- Backtest results typically degrade 20-30% in live trading
- Slippage and fees significantly impact profitability
- Market conditions change; models need retraining
- No strategy works all the time
- Risk management is critical

## 🛠️ Technical Details

### System Requirements
- **Python**: 3.9 or higher
- **RAM**: 8GB minimum, 16GB recommended
- **Disk**: 5GB free space
- **GPU**: Optional but recommended for faster training

### Dependencies
- PyTorch 2.0+
- Pandas, NumPy, Matplotlib
- mmcv, Ray (for RL)
- See `requirements.txt` for full list

### Training Time Estimates
- **DQN**: 10-20 minutes (5 epochs)
- **PPO**: 15-30 minutes (5 epochs)
- **SAC**: 15-35 minutes (5 epochs)

Times vary based on hardware. GPU acceleration recommended.

## 🐛 Troubleshooting

### Common Issues

**1. "Module not found" errors**
```bash
# Make sure you installed dependencies
pip install -r requirements.txt
# And TradeMaster
pip install -e .
```

**2. "CUDA out of memory"**
```python
# Reduce batch size in config
config['batch_size'] = 32  # Instead of 64
```

**3. "Data not found"**
```bash
# Make sure you're in the right directory
cd rl_intraday_trading_notebooks
# Check if data exists
ls -la data/MCL-1m/
```

**4. Training is too slow**
```python
# Reduce epochs for testing
config['trainer']['epochs'] = 2  # Instead of 5
```

## 📖 Additional Resources

### RL Theory
- [Spinning Up in Deep RL](https://spinningup.openai.com/) - OpenAI's RL guide
- [Sutton & Barto Book](http://incompleteideas.net/book/) - RL bible

### Trading & Finance
- [Advances in Financial ML](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086) - Marcos López de Prado
- [Quantitative Trading](http://epchan.blogspot.com/) - Ernest Chan's blog

### TradeMaster
- [TradeMaster Paper](https://arxiv.org/abs/2211.09893) - Official paper
- [TradeMaster Docs](https://trademaster.readthedocs.io/) - Full documentation
- [TradeMaster GitHub](https://github.com/TradeMaster-NTU/TradeMaster) - Source code

### Communities
- [r/algotrading](https://reddit.com/r/algotrading) - Algorithmic trading
- [r/reinforcementlearning](https://reddit.com/r/reinforcementlearning) - RL discussions
- [QuantConnect](https://www.quantconnect.com/) - Backtesting platform

## 🤝 Contributing

Found a bug? Have a suggestion? Want to add a notebook?

1. Open an issue on GitHub
2. Submit a pull request
3. Share your experiments!

## 📝 Citation

If you use these notebooks in your research, please cite:

```bibtex
@article{trademaster2023,
  title={TradeMaster: A Holistic Quantitative Trading Platform Empowered by Reinforcement Learning},
  author={Sun, Shuo and others},
  journal={NeurIPS},
  year={2023}
}
```

## ⭐ Acknowledgments

This tutorial series is built on top of the excellent [TradeMaster](https://github.com/TradeMaster-NTU/TradeMaster) platform by the AMI group at NTU.

Special thanks to:
- TradeMaster team for the awesome platform
- OpenAI for RL research and Spinning Up
- The RL and quantitative trading communities

## 📧 Contact & Support

- **Issues**: Open a GitHub issue
- **Questions**: Use GitHub Discussions
- **TradeMaster**: TradeMaster.NTU@gmail.com

## 📜 License

This project follows the same license as TradeMaster. See LICENSE file for details.

---

## 🎯 Ready to Start?

1. **Install dependencies**: `pip install -r ../requirements.txt`
2. **Open Notebook 1**: Start with data exploration
3. **Follow the series**: Complete all 5 notebooks in order
4. **Experiment**: Try different contracts and parameters
5. **Build your strategy**: Apply what you've learned!

### 🚀 Let's Trade with AI!

**Remember**: 
- Start small
- Paper trade first
- Risk management is key
- Keep learning

**Good luck with your RL trading journey! 📈🤖**

---

*Last updated: January 2026*
*Version: 1.0.0*
