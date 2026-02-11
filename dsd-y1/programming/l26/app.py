import matplotlib.pyplot as plt

# revenue fore cast
x = ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul"]
y = [0, 36500, 28000, 27500, 41000, 49500]

plt.style.use(["dark_background", "./dsd-y1/L26/revenueForecast.mplstyle"])

plt.plot(x, y)

plt.grid(True)

plt.title("2026 1st and 2nd Quater Revenue Forecast")

plt.xlabel("Time Month")
plt.ylabel("Revenue £")

plt.show()

