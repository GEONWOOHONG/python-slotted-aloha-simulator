# python-slotted-aloha-simulator

> Python implementation of the Slotted ALOHA protocol, adapted from a C++ demo by Shivam Prasad.

---

## ✨ What it does

- Places senders randomly on an n × m grid  
- Lets only mutually reachable nodes join  
- Runs classic Slotted ALOHA: collision detection, random backoff, max‐retry Kmax
- Prints per-slot log and final stats

---

## 🚀 Run it

```bash
python simulator.py
```

The program will ask, in order:

```text
n  m               # grid size
min max            # comm. range per node
senders            # number of nodes
Kmax               # max retransmissions
Tp                 # timeout (UI only, kept for parity)
slots              # number of time slots to simulate
```

No extra libraries needed – Python 3.8+ and the standard library are enough.

## 🔎 Example

```text
SLOT = 1
Collision occurred!!!
Sender 1 Blocked. (waits for 2 time slots, K=1)

SLOT = 2
Sender 3's packet successfully transmitted!

...
Total number of packets = 40
Total number of packets sent = 10
```

## 📝 Reference
- Based on the original C++ demo by [Shivam Prasad](https://github.com/shivam2296/Slotted-ALOHA).

This repo is for educational use only.  
Please check the original project’s license for other uses.
