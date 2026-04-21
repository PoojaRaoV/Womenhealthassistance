import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Register() {

  const [data, setData] = useState({
    name: "",
    email: "",
    password: ""
  });

  const navigate = useNavigate();   // ✅ INSIDE FUNCTION

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://localhost:5000/register", data);

      navigate("/login");   // ✅ redirect

    } catch (error) {
        alert("Error registering user");
      console.log(error);
      alert("Error");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2>Register</h2>

        <form onSubmit={handleSubmit}>
          <input
            placeholder="Name"
            style={styles.input}
            onChange={(e) =>
              setData({ ...data, name: e.target.value })
            }
          />

          <input
            placeholder="Email"
            style={styles.input}
            onChange={(e) =>
              setData({ ...data, email: e.target.value })
            }
          />

          <input
            type="password"
            placeholder="Password"
            style={styles.input}
            onChange={(e) =>
              setData({ ...data, password: e.target.value })
            }
          />

          <button type="submit" style={styles.button}>
            Register
          </button>
        </form>
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f2f2f2"
  },
  card: {
    background: "#fff",
    padding: "30px",
    borderRadius: "12px",
    boxShadow: "0px 4px 15px rgba(0,0,0,0.1)",
    width: "320px",
    textAlign: "center"
  },
  title: {
    marginBottom: "20px",
    fontWeight: "bold"
  },
  input: {
    width: "100%",
    padding: "10px",
    margin: "10px 0",
    borderRadius: "6px",
    border: "1px solid #ccc"
  },
  greenButton: {
    width: "100%",
    padding: "10px",
    backgroundColor: "green",
    color: "#fff",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer"
  },
  blueButton: {
    width: "100%",
    padding: "10px",
    backgroundColor: "#4CAF50",
    color: "#fff",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer"
  },
  linkText: {
    marginTop: "10px",
    fontSize: "14px"
  },
  link: {
    color: "green",
    cursor: "pointer",
    textDecoration: "underline"
  }
};
export default Register;