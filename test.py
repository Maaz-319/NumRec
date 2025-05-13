import tensorflow as tf  
import numpy as np  


image_path = "test.png"

# Preprocess the uploaded image
img = preprocess_image(image_path)


interpreter.set_tensor(input_details[0]['index'], img)
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
predicted_class = np.argmax(output_data)
confidence = np.max(output_data)

# Get the emotion label using the predicted class index
predicted_emotion = list(inverse_labels.keys())[predicted_class] # Get the emotion label corresponding to the predicted class index.


print("Predicted Emotion:", predicted_emotion) # Print the predicted emotion label.
print(f"Confidence: {confidence:.2f}")