# Quick Start Guide - RL for Intraday Trading

## 🎯 Get Started in 5 Minutes!

### Step 1: Install Dependencies
```bash
cd /path/to/TradeMasterChill
pip install -r requirements.txt
pip install -e .
```

### Step 2: Navigate to Notebooks
```bash
cd rl_intraday_trading_notebooks
```

### Step 3: Launch Jupyter
```bash
jupyter notebook
```

### Step 4: Start Learning!
Open the notebooks in order:
1. **1_Data_Exploration_and_Preparation.ipynb** - Understand your data
2. **2_Simple_DQN_Training.ipynb** - Train your first RL agent
3. **3_PPO_Training.ipynb** - Learn stable policy-based RL
4. **4_SAC_Training.ipynb** - Master state-of-the-art RL
5. **5_Advanced_Features.ipynb** - Production-ready strategies

## 📊 What You'll Build

By the end of this series, you'll be able to:
- ✅ Train RL agents (DQN, PPO, SAC) for intraday trading
- ✅ Implement risk management strategies
- ✅ Use advanced technical indicators
- ✅ Compare algorithm performance
- ✅ Deploy production-ready trading systems

## 🚀 Available Datasets

All data is preprocessed and ready to use:
- **MCL-1m**: Micro Crude Oil (351K records)
- **MGC-1m**: Micro Gold (355K records)
- **mes-1m**: Micro S&P 500 (350K records)
- **ng**: Natural Gas (336K records)
- **si**: Silver (343K records)

## ⏱️ Time Commitment

- **Notebook 1**: 15-20 min (no training)
- **Notebook 2**: 30-45 min (includes DQN training)
- **Notebook 3**: 30-45 min (includes PPO training)
- **Notebook 4**: 30-45 min (includes SAC training)
- **Notebook 5**: 45-60 min (exploration, no training)

**Total**: ~3 hours for complete mastery!

## 💡 Pro Tips

1. **Run cells sequentially** - Don't skip ahead
2. **Read the explanations** - Understanding > Speed
3. **Experiment** - Change parameters and see what happens
4. **Start simple** - Master DQN before moving to SAC
5. **Use small epochs** - Set epochs=2 for quick testing

## 🆘 Need Help?

- **Installation issues**: Check `requirements.txt`
- **CUDA errors**: Reduce batch_size to 32
- **Slow training**: Reduce epochs to 2-3 for testing
- **Data not found**: Run from `rl_intraday_trading_notebooks/` directory

## 🎓 Learning Path

### Beginner Track (Week 1)
- Day 1: Notebook 1 + read theory
- Day 2-3: Notebook 2 (DQN)
- Day 4-5: Experiment with DQN

### Intermediate Track (Week 2)
- Day 1-2: Notebook 3 (PPO)
- Day 3-4: Notebook 4 (SAC)
- Day 5: Compare all algorithms

### Advanced Track (Week 3)
- Day 1-3: Notebook 5 (Advanced features)
- Day 4-5: Build your own strategy!

## 📈 Success Metrics

After completing the notebooks, you should be able to:
- [ ] Explain how RL works for trading
- [ ] Train agents that beat buy-and-hold
- [ ] Implement proper risk management
- [ ] Understand Sharpe ratio and drawdowns
- [ ] Choose the right algorithm for your needs

## ⚠️ Remember

- **This is educational** - Not financial advice
- **Paper trade first** - Don't risk real money immediately
- **Risk management** - Always use stop-losses
- **Backtest properly** - Multiple time periods and conditions

## 🚀 Ready? Let's Go!

Open `1_Data_Exploration_and_Preparation.ipynb` and start your RL journey!

**Good luck! 📈🤖**
