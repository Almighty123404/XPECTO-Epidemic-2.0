# Strategy Evaluation Report

## Summary

| Strategy                |    Score | Grade   | Population   | GDP   | Infection Control   | Resource Efficiency   |
|:------------------------|---------:|:--------|:-------------|:------|:--------------------|:----------------------|
| Static Strategy         | 0.735009 | B+      | 96.5%        | 33.9% | 60.6%               | 1.0%                  |
| RL-Inspired Strategy    | 0.626187 | B-      | 91.8%        | 15.9% | 53.3%               | 0.4%                  |
| Response Curve Strategy | 0.196613 | F       | 66.1%        | 8.9%  | 0.0%                | 0.6%                  |
| Phase-Based Strategy    | 0.115668 | F       | 0.0%         | 67.4% | 0.0%                | 0.5%                  |


## Detailed Analysis

### Static Strategy

- **Score**: 0.7350 (Grade: B+)
- **Population Survived**: 96.5%
- **GDP Preserved**: 33.9%
- **Infection Control**: 60.6%
- **Variant Control**: 1.00

**Performance Insights:**

- Multi-objective Balance: 0.597


### Phase-Based Strategy

- **Score**: 0.1157 (Grade: F)
- **Population Survived**: 0.0%
- **GDP Preserved**: 67.4%
- **Infection Control**: 0.0%
- **Variant Control**: 0.23

**Performance Insights:**

- Multi-objective Balance: 0.000


### Response Curve Strategy

- **Score**: 0.1966 (Grade: F)
- **Population Survived**: 66.1%
- **GDP Preserved**: 8.9%
- **Infection Control**: 0.0%
- **Variant Control**: 0.25

**Performance Insights:**

- Multi-objective Balance: 0.081


### RL-Inspired Strategy

- **Score**: 0.6262 (Grade: B-)
- **Population Survived**: 91.8%
- **GDP Preserved**: 15.9%
- **Infection Control**: 53.3%
- **Variant Control**: 0.26

**Performance Insights:**

- Multi-objective Balance: 0.458

