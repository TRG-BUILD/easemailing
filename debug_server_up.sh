echo "Listening to emails sent to localhost:1025:"
python -m smtpd -c DebuggingServer -n localhost:1025 
