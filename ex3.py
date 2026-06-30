import matplotlib.pyplot as plt

# Figure
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# -------------------------
# Left: Independent musicians
# -------------------------
ax = axes[0]

players = {
    "Violin": (0, 2),
    "Flute": (2, 2),
    "Cello": (0, 0),
    "Piano": (2, 0)
}

for name, (x, y) in players.items():
    ax.scatter(x, y, s=600)
    ax.text(x, y-0.25, name,
            ha="center", fontsize=10)

ax.set_title("Low Integrated Information\n(Independent Performance)",
             fontsize=13)

ax.text(1, -0.8,
        "Each musician plays independently.\n"
        "Information exists, but it is not integrated.",
        ha="center", fontsize=10)

ax.set_xlim(-1, 3)
ax.set_ylim(-1.5, 3)
ax.set_xticks([])
ax.set_yticks([])

# -------------------------
# Right: Orchestra
# -------------------------
ax = axes[1]

conductor = (1, 2.7)

ax.scatter(*conductor, s=700)
ax.text(conductor[0], conductor[1]+0.2,
        "Conductor",
        ha="center",
        fontsize=11)

for name, (x, y) in players.items():
    ax.scatter(x, y, s=600)
    ax.text(x, y-0.25, name,
            ha="center", fontsize=10)

    # conductor to player
    ax.plot([conductor[0], x],
            [conductor[1], y],
            linewidth=2)

# connections among musicians
connections = [
    ("Violin", "Flute"),
    ("Violin", "Cello"),
    ("Flute", "Piano"),
    ("Cello", "Piano")
]

for a, b in connections:
    x1, y1 = players[a]
    x2, y2 = players[b]
    ax.plot([x1, x2], [y1, y2],
            linestyle="--",
            linewidth=1)

ax.set_title("High Integrated Information\n(Orchestra)",
             fontsize=13)

ax.text(1, -0.8,
        "Musicians coordinate with each other.\n"
        "The performance emerges as one integrated whole.",
        ha="center", fontsize=10)

ax.set_xlim(-1, 3)
ax.set_ylim(-1.5, 3.5)
ax.set_xticks([])
ax.set_yticks([])

plt.suptitle(
    "Illustration of Integrated Information Theory (IIT)",
    fontsize=16
)

plt.tight_layout()
plt.show()