import streamlit as st
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import io

# QR Code generate function
def generate_qr_code(data: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    return img

# QR Code decode function
def decode_qr_code(img: Image):
    decoded_objects = decode(img)
    result = []
    for obj in decoded_objects:
        result.append(obj.data.decode('utf-8'))
    return result

# Streamlit app layout
def main():
    # Set page config with centered layout (without sidebar)
    st.set_page_config(page_title="QR Code Generator & Decoder", page_icon="🔑", layout="centered", initial_sidebar_state="collapsed")
    
    st.title("QR Code Generator & Decoder 🔑")
    st.markdown("<h2 style='color: #2e6c82;'>Welcome to the QR Code Encoder & Decoder App! 🌟</h2>", unsafe_allow_html=True)
    
    # QR Code Generator Section
    st.header("🔸 QR Code Generator")
    data_to_encode = st.text_input("Enter text or URL for QR Code 📝:")
    
    if data_to_encode:
        qr_img = generate_qr_code(data_to_encode)
        
        # Convert PIL image to bytes before displaying
        img_byte_arr = io.BytesIO()
        qr_img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        st.image(img_byte_arr, caption="Generated QR Code 📲", use_container_width=True)
        st.success("QR Code Generated Successfully! 🎉")
    
    # QR Code Decoder Section
    st.header("🔹 QR Code Decoder")
    uploaded_file = st.file_uploader("Upload a QR Code Image 📸", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        decoded_data = decode_qr_code(img)
        
        if decoded_data:
            st.success("Decoded Successfully! 🥳")
            for data in decoded_data:
                st.write(f"Decoded Data: **{data}** 💡")
        else:
            st.warning("No QR Code found in the image! ❌")

    # Footer
    st.markdown("<br><br><h5 style='text-align: center; color: #666;'>Created by Nimra ✨💻😊</h5>", unsafe_allow_html=True)

# Run Streamlit app 
if __name__ == "__main__":
    main()
