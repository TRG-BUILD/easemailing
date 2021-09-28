echo "Listening to emails sent to localhost:1025:"
python -u -m smtpd -c DebuggingServer -n localhost:1025 > smtp.log
