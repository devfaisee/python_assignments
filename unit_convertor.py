import streamlit as st
import random

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.title("🔄 Google-Style Unit Converter")
st.caption("Simple, Fast, and a Little Fun! 🚀")

st.divider()

# --- converssionz start here ---
conversion_factors = {
    "Length (Meters ↔️ Feet)": {
        "meters to feet": 3.28084,
        "feet to meters": 0.3048
    },
    "Weight (Kilograms ↔️ Pounds)": {
        "kilograms to pounds": 2.20462,
        "pounds to kilograms": 0.453592
    },
    "Temperature (Celsius ↔️ Fahrenheit)": {
        "celsius to fahrenheit": (lambda c: (c * 9/5) + 32),
        "fahrenheit to celsius": (lambda f: (f - 32) * 5/9)
    },
    "Speed (Km/h ↔️ Mph)": {
        "km/h to mph": 0.621371,
        "mph to km/h": 1.60934
    }
}

fun_facts = [
    "🌎 Earth’s circumference is about 40,075 kilometers!",
    "📏 The word 'inch' comes from the Latin word 'uncia,' meaning one-twelfth!",
    "🏋️ 1 pound is legally defined as exactly 0.45359237 kilograms!",
    "📏 There are exactly 2.54 centimeters in an inch!",
    "🛩️ The speed of sound at sea level is about 343 meters per second!",
    "🧊 Absolute zero is the lowest possible temperature: -273.15°C!",
    "🔭 Light takes about 8 minutes to travel from the Sun to Earth!",
    "⚡ A bolt of lightning is about 5 times hotter than the surface of the Sun!",
    "🏎️ Formula 1 cars can reach speeds of over 370 km/h!",
    "🐢 The fastest recorded tortoise speed is 0.28 km/h!",
    "🌬️ Wind speeds above 119 km/h are considered a hurricane!",
    "🌡️ The Celsius scale is based on the freezing and boiling points of water!",
    "🪨 The heaviest rock ever moved by humans weighed about 1,000 tons!",
    "🕰️ The atomic clock is so precise it would lose 1 second every 100 million years!",
    "🌟 The nearest star to Earth is about 40 trillion kilometers away!",
    "🧱 1 cubic meter of concrete weighs around 2,400 kilograms!",
    "🍃 The fastest growing plant is bamboo, growing up to 91 cm in one day!",
    "💨 A sneeze can travel at speeds of up to 160 km/h!",
    "🌌 The Milky Way galaxy is about 105,700 light-years across!",
    "🐋 A blue whale’s tongue can weigh as much as an elephant!",
    "🛡️ The thickest ice measured on Earth was over 4,776 meters thick!",
    "🚀 The fastest manned vehicle was Apollo 10, reaching 39,897 km/h!",
    "📡 Radio waves travel at the speed of light!",
    "🔢 There are 1,000 meters in a kilometer — exactly by definition!",
    "🥶 Antarctica holds the record for the lowest temperature: -89.2°C!",
    "🌕 The Moon’s diameter is about 3,474 kilometers!",
    "🛣️ The longest road in the world is the Pan-American Highway, about 30,000 km long!",
    "⚖️ The metric system was first adopted in France in 1795!",
    "🌧️ The world record for rainfall in one minute is 31.2 mm!",
    "🧪 One mole of substance contains exactly 6.022 × 10²³ particles!",
    "🚢 The largest cruise ship weighs over 228,000 gross tons!",
    "🎈 Helium is lighter than air by about 0.1785 grams per liter!",
    "🐎 A galloping horse can run at about 55 km/h!",
    "🎯 The longest sniper kill was recorded at 3,540 meters!",
    "🧊 Water expands about 9% when it freezes!",
    "🛰️ The International Space Station travels at about 28,000 km/h!",
    "🎢 The tallest roller coaster in the world is 139 meters tall!",
    "🧲 The strongest magnet in the world can lift an aircraft carrier!",
    "🏔️ Mount Everest grows about 4 millimeters higher every year!",
    "🐆 The cheetah is the fastest land animal, reaching 112 km/h!",
    "🌍 71% of Earth's surface is covered by water!",
    "🦒 A giraffe’s heart weighs about 11 kilograms!",
    "🛑 A typical red traffic light is about 30,000 lumens in brightness!",
    "🦕 Some dinosaurs grew up to 40 meters long!",
    "🌲 The tallest tree on Earth is over 115 meters tall!",
    "🛬 The longest non-stop flight lasted over 19 hours!",
    "🔥 The hottest temperature ever recorded on Earth was 56.7°C!",
    "🕳️ The deepest part of the ocean is about 10,984 meters deep!",
    "🍕 The world's largest pizza had a diameter of 39.6 meters!",
    "🎼 The speed of sound in water is about 1,484 meters per second!",
    "💧 1 liter of water weighs exactly 1 kilogram at 4°C!",
    "🌄 Light travels 299,792 kilometers per second in a vacuum!",
    "🛹 The fastest skateboard speed was recorded at 146.73 km/h!",
    "🦅 The peregrine falcon dives at speeds over 320 km/h!",
    "🔋 The energy in a bolt of lightning could power a home for a month!",
    "🌦️ The highest rainfall ever in a year was over 26,000 mm!",
    "📈 The metric ton is exactly 1,000 kilograms!",
    "🛤️ The longest railway network is over 250,000 km long!",
    "🐘 An elephant's trunk can lift about 270 kilograms!",
    "🎇 The hottest part of a fire can reach 1,100°C or more!",
    "🌡️ Mercury thermometers work because mercury expands with heat!",
    "🏄 The biggest ocean wave surfed was 26.2 meters tall!",
    "💨 A Category 5 hurricane has winds over 252 km/h!",
    "🌍 Earth's magnetic field is weakening by about 5% every century!",
    "🛢️ A barrel of oil is about 159 liters!",
    "🪂 The highest skydive was from a height of 39 kilometers!",
    "🧱 Bricks absorb about 15% of their weight in water!",
    "🧊 The largest iceberg ever recorded was bigger than Jamaica!",
    "🔭 The Hubble Space Telescope orbits at 547 kilometers above Earth!",
    "🌋 Lava can flow at speeds up to 60 km/h!",
    "📏 The micrometer is one-millionth of a meter!",
    "🌫️ Visibility less than 1 kilometer is considered fog!",
    "🛒 The average shopping cart weighs about 13 kilograms!",
    "🦏 Rhinos can run up to 50 km/h despite their size!",
    "🌡️ Temperature affects the speed of sound — faster in warmer air!",
    "🏔️ Mount Everest's summit is 8,848 meters above sea level!",
    "🚂 The fastest steam locomotive reached 202 km/h!",
    "📦 The first package weighed on a FedEx scale weighed less than 1 kg!",
    "🛰️ GPS satellites orbit about 20,200 kilometers above Earth!",
    "💥 The Tunguska explosion in 1908 flattened 2,000 square kilometers!",
    "🏄‍♂️ Water pressure increases by 1 atmosphere every 10 meters deep!",
    "🌏 Asia is the largest continent, covering 30% of Earth's land!",
    "🌡️ A Celsius degree is 1.8 times larger than a Fahrenheit degree!",
    "🔋 1 AA battery stores about 9,000 joules of energy!",
    "🌉 The Golden Gate Bridge is about 2.7 kilometers long!",
    "🛸 UFO sightings peaked at speeds 'too fast to measure'!",
    "🏛️ The Roman mile was about 1,480 meters!",
    "🧮 The kilogram is defined by Planck’s constant since 2019!",
    "🌙 A day on the Moon lasts about 29.5 Earth days!",
    "🪨 The heaviest dinosaur fossil weighed about 77 tons!",
    "🏎️ Top fuel dragsters can accelerate to 531 km/h in under 5 seconds!",
    "🧊 Ice at -40°C is twice as hard as ice at 0°C!",
    "🧵 A nanometer is one-billionth of a meter!",
    "🚜 The world's largest tire is over 4 meters tall!",
    "🏔️ The pressure at Mount Everest’s summit is about 1/3 that at sea level!",
    "🦅 The wandering albatross can fly 10,000 km without stopping!",
    "🎢 Some roller coasters pull over 6 Gs in loops!",
    "🏝️ The Mariana Trench is deeper than Mount Everest is tall!",
    "🛩️ The Wright Brothers' first flight traveled only 36 meters!",




]

# --- functons idk how it  does but it does so yeah ---
def convert_units(category, direction, value):
    if "Temperature" in category:
        func = conversion_factors[category][direction]
        return func(value)
    else:
        factor = conversion_factors[category][direction]
        return value * factor

# --- styling with chacha gpt ---
st.subheader("1️⃣ Choose Conversion Type:")
category = st.selectbox("Select Category", list(conversion_factors.keys()))

st.subheader("2️⃣ Choose Direction:")
options = list(conversion_factors[category].keys())
direction = st.radio("Select Direction", options)

st.subheader("3️⃣ Enter Value:")
value = st.number_input("Input the value you want to convert", format="%.4f")

st.subheader("4️⃣ Get Result:")
if st.button("🔁 Convert Now"):
    with st.spinner('Calculating...✨'):
        result = convert_units(category, direction, value)
    st.success(f"🎯 Converted Value: {result:.4f}")

    # Random Fun Fact
    st.divider()
    st.info(random.choice(fun_facts))




st.divider()
st.caption("Made with ❤️ using Python & Streamlit By Faisal Ali")

