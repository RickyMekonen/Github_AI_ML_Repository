# Coupon Acceptance Analysis

## Overview

This project analyzes the acceptance rates of coupons in various driving scenarios. The analysis reveals that drivers heading home in the same direction as the coupon (which is five minutes away) show a higher acceptance rate compared to other scenarios. Conversely, when drivers are heading in the opposite direction and the distance increases, the acceptance rate declines.

## Data Source

The data used for this analysis is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) and was collected through a survey on Amazon Mechanical Turk. The survey presents various driving scenarios, including:

- Destination
- Current time
- Weather conditions
- Passenger status

Respondents were asked whether they would accept a coupon if they were the driver. Responses indicating that the user would drive there "right away" or "later before the coupon expires" were labeled as Y = 1, while responses indicating "no, I do not want the coupon" were labeled as Y = 0.

## Coupon Types

The survey examined five different types of coupons:

1. Less expensive restaurants (under $20)
2. Coffee houses
3. Carry-out & take-away
4. Bars
5. More expensive restaurants ($20 - $50)

## Conclusion

The analysis indicates that proximity and directionality significantly impact coupon acceptance rates among drivers. Further exploration could provide deeper insights into consumer behavior related to coupon usage.

## Getting Started

1. Clone the repository to your local machine.
2. Install any necessary dependencies (if applicable).
3. Run the analysis scripts to explore the data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Mekonen - Project lead
- LLearning facilitator
