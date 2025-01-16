db = db.getSiblingDB('quiz_platform_app'); // Switch to the quiz_platform_app database

// Create the 'users' collection with a sample user
db.users.insertOne({
  username: "testuser",
  password: "testpassword"
});

// Create the 'quizzes' collection and insert the provided quiz data
db.quizzes.insertMany([
  {
    _id: 1,
    question: "What is the capital of France?",
    option_a: "Paris",
    option_b: "London",
    option_c: "Berlin",
    option_d: "Madrid",
    correct_option: "A"
  },
  {
    _id: 2,
    question: "What is the capital of Germany?",
    option_a: "Paris",
    option_b: "London",
    option_c: "Berlin",
    option_d: "Madrid",
    correct_option: "C"
  },
  {
    _id: 3,
    question: "What is the capital of Spain?",
    option_a: "Paris",
    option_b: "London",
    option_c: "Berlin",
    option_d: "Madrid",
    correct_option: "D"
  },
  {
    _id: 4,
    question: "What is the capital of England?",
    option_a: "Paris",
    option_b: "London",
    option_c: "Berlin",
    option_d: "Madrid",
    correct_option: "B"
  }
]);
