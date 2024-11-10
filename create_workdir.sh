mkdir -p workdir
cd workdir || { echo "Failed to enter workdir"; exit 1; }

mv ../1_web_basics .
mv ../2_SDE .
mv ../3_HTML_inj .
mv ../4_XSS .
mv ../5_XSS .
mv ../6_CSFR .

python3 -m venv v_env
source v_env/bin/activate
if [ -d "v_env/bin" ] && [ -f "v_env/pyvenv.cfg" ]; then
    echo -e "virtual environment successfully activated"
else
    echo -e "virtual environment not activated"
    exit 1
fi

pip install --upgrade pip
pip install Flask

echo -e "setup completed"
