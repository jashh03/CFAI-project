grid = [
['S','0','0','X','0'],
['0','X','0','X','0'],
['0','X','0','0','0'],
['0','0','X','X','0'],
['0','0','0','0','G']
]

prior = 0.6
sensor_accuracy = 0.8
evidence = 0.7

posterior = (sensor_accuracy * prior) / evidence

estimated_position = (2,2)

print("===== CO5 : Bayesian Localization =====\n")

print("GRID:")
for row in grid:
    print(row)

print("\nSensor Reading =", estimated_position)

print("\nPrior Probability =", prior)
print("Sensor Accuracy =", sensor_accuracy)
print("Posterior Probability =", round(posterior,3))

print("\nEstimated Robot Position:")
print(estimated_position)

print("\nLocalization Updated Successfully")