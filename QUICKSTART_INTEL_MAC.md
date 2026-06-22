# LocalLens Quick Start — Intel Mac

Run LocalLens on your Intel-based Mac from source.

## 1. Install Prerequisites

Open Terminal and run:

```bash
# Install Xcode command-line tools
xcode-select --install

# Install Homebrew dependencies
brew install cmake dlib imagemagick

# Install Rust (if not already installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

# Configure Rust for Intel Mac
rustup target add x86_64-apple-darwin
rustup default stable-x86_64-apple-darwin

# Verify
cargo --version
rustc --version
```

## 2. Set Up Python Backend

From the repo root:

```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Start the backend server
python main.py
```

You should see:
```
Scheduler daemon launched (PID xxxx)...
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Leave this terminal running.**

## 3. Set Up & Run Frontend (New Terminal)

Open a **new Terminal tab/window**:

```bash
cd frontend

# Install dependencies
pnpm install

# Approve build scripts if prompted
pnpm approve-builds

# Start Tauri dev server
pnpm run tauri dev
```

The desktop app should open. You'll see:
- Backend connection status
- Face recognition availability
- Ready to organize photos

## 4. Using LocalLens

### Scan External Drive + Keep Index Local

1. **Pick source**: Click "Browse Source" → select a folder on your external drive
2. **Pick destination**: Click "Browse Destination" → select a local folder
3. **Choose operation**: Toggle **Copy** (recommended for external drives)
4. **Pick sort method**: Date, Location, or People
5. **Click "Start Organizing"**

Your indexing data (metadata DB, face encodings, presets) is stored locally at:
```
~/Library/Application Support/LocalLens/
```

### Force Custom Index Location

If you want indexing on a specific local disk, start the backend with:

```bash
LOCALLENS_DATA_DIR="/Volumes/YourLocalDrive/LocalLensData" python main.py
```

Then follow steps 2–4 above.

## 5. Enroll Faces (Optional)

1. In the app, go to **Enrollment**
2. Click **Select Images** → pick photos of a person
3. Enter their name → **Add to Queue**
4. Repeat for more people
5. Click **Start Batch Enrollment**

Next time you sort by "People", LocalLens will recognize them.

## Troubleshooting

### Backend won't start
- Check Python version: `python3 --version` (need 3.11+)
- Reinstall dependencies: `pip install -r requirements.txt`
- Check for port conflicts: `lsof -i :8000`

### Tauri dev fails with `cargo metadata` error
```bash
source "$HOME/.cargo/env"
rustup target add x86_64-apple-darwin
cd frontend
node ensure-backend.js
pnpm run tauri dev
```

### "Backend connection failed" in app
- Verify backend is running in first terminal (see step 2)
- Check `http://127.0.0.1:8000/api/health` in browser
- Backend must start before opening the app

### Face recognition unavailable
- Ensure `dlib` installed: `brew list dlib`
- Reinstall if needed: `brew reinstall dlib`
- Reinstall Python deps: `pip install face_recognition`

## Next Steps

- **Read full docs**: See `Local Lens - Installation & Setup Guid.md`
- **Report issues**: [GitHub Issues](https://github.com/ashesbloom/LocalLens/issues)
- **Build for release**: See `scripts/build-reproducible.sh`

---

**Happy organizing!** 📸
