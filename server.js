const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();

// ✅ Middleware
app.use(cors());
app.use(express.json());

// ✅ MongoDB Connection
mongoose.connect("mongodb://127.0.0.1:27017/userDB")
  .then(() => console.log("MongoDB Connected"))
  .catch(err => console.log(err));

// ================= USER SCHEMA =================
const UserSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
});

const User = mongoose.model("User", UserSchema);

// ================= HEALTH DATA SCHEMA =================
const DataSchema = new mongoose.Schema({
  name: String,
  age: String,
  weight: String,
  height: String,
  symptoms: String,
});

const DataModel = mongoose.model("HealthData", DataSchema);

// ================= APIs =================

// ✅ Register API
app.post("/register", async (req, res) => {
  try {
    const user = new User(req.body);
    await user.save();

    res.json({ message: "User Registered Successfully" });
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Error registering user" });
  }
});

// ✅ Login API
app.post("/login", async (req, res) => {
  try {
    const { email, password } = req.body;

    const user = await User.findOne({ email, password });

    if (user) {
      res.json({ message: "Login Success" });
    } else {
      res.status(401).json({ message: "Invalid credentials" });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Login error" });
  }
});

// ✅ ADD DATA API (🔥 YOUR MAIN FEATURE)
app.post("/addData", async (req, res) => {
  try {
    const newData = new DataModel(req.body);
    await newData.save();

    res.json({ message: "Health Data Saved Successfully" });
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Error saving data" });
  }
});

// ================= SERVER =================
app.listen(5000, () => {
  console.log("Server running on port 5000");
});