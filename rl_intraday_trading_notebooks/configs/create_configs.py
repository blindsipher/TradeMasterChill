"""
Configuration Builder for RL Intraday Trading

This module creates configuration files for different futures contracts
"""

from pathlib import Path

# Contract information
CONTRACTS = {
    'MCL-1m': {'name': 'Micro Crude Oil', 'initial_amount': 100000},
    'MGC-1m': {'name': 'Micro Gold', 'initial_amount': 100000},
    'mes-1m': {'name': 'Micro E-mini S&P 500', 'initial_amount': 100000},
    'ng': {'name': 'Natural Gas', 'initial_amount': 100000},
    'si': {'name': 'Silver', 'initial_amount': 100000},
}

# Common configuration template
def create_config(contract_code):
    """Create configuration dictionary for a contract"""
    
    contract_info = CONTRACTS[contract_code]
    data_path = f'../data/{contract_code}'
    
    config = {
        'contract': contract_code,
        'contract_name': contract_info['name'],
        
        # Data configuration
        'data': {
            'train_path': f'{data_path}/train.csv',
            'valid_path': f'{data_path}/valid.csv',
            'test_path': f'{data_path}/test.csv',
            'tech_indicator_list': [
                'high', 'low', 'open', 'close', 'adjcp',
                'zopen', 'zhigh', 'zlow', 'zadjcp', 'zclose',
                'zd_5', 'zd_10', 'zd_15', 'zd_20', 'zd_25', 'zd_30'
            ],
            'backward_num_day': 5,  # Look back 5 periods
            'forward_num_day': 5,   # Look forward 5 periods
            'initial_amount': contract_info['initial_amount'],
            'transaction_cost_pct': 0.001,  # 0.1% transaction cost
            'max_volume': 1,  # Max 1 contract per trade
        },
        
        # Agent configuration (DQN)
        'dqn_agent': {
            'max_step': 10000,
            'reward_scale': 1,
            'gamma': 0.9,  # Discount factor
            'batch_size': 64,
            'learning_rate': 0.001,
            'epsilon_start': 1.0,  # Exploration rate at start
            'epsilon_end': 0.01,   # Minimum exploration rate
            'epsilon_decay': 0.995,
            'target_update': 10,   # Update target network every 10 episodes
        },
        
        # Network configuration
        'network': {
            'state_dim': 82,  # 16 indicators * 5 periods + 2 (cash, position)
            'action_dim': 3,  # 0: Sell, 1: Hold, 2: Buy
            'hidden_dims': [64, 32],
        },
        
        # Training configuration
        'training': {
            'epochs': 20,
            'buffer_size': 100000,
            'batch_size': 64,
            'horizon_len': 128,
            'num_threads': 4,
        },
        
        # Evaluation configuration
        'evaluation': {
            'initial_amount': contract_info['initial_amount'],
            'transaction_cost_pct': 0.001,
        }
    }
    
    return config


def main():
    """Generate all configuration files"""
    config_dir = Path(__file__).parent
    
    for contract_code in CONTRACTS.keys():
        config = create_config(contract_code)
        
        # Save as Python dict (can be imported)
        config_file = config_dir / f'config_{contract_code}.py'
        with open(config_file, 'w') as f:
            f.write(f'"""Configuration for {config["contract_name"]} ({contract_code})"""\n\n')
            f.write('CONFIG = ')
            f.write(str(config).replace("'", '"'))
        
        print(f"✅ Created config for {contract_code}")
    
    print(f"\n✅ All configuration files created in {config_dir}")


if __name__ == '__main__':
    main()
