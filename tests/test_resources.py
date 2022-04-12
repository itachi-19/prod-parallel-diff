icapture = 'input/icapture.csv'
fidstp = 'input/fidstp.csv'

icapture_msg1 = '<NewTrade>\n' \
        '<id>5001</id>\n' \
        '<trade>\n' \
        '        <cparty>Black Rock</cparty>\n' \
        '</trade>\n' \
        '</NewTrade>'
icapture_msg2 = '<NewTrade>\n' \
        '<id>50023</id>\n' \
        '<trade>\n' \
        '        <cparty>Bloomberg132</cparty>\n' \
        '</trade>\n' \
        '</NewTrade>'

icapture_msg3 = '<NewTrade>\n' \
        '<id>5003</id>\n' \
        '<trade>\n' \
        '        <cparty>Bloomberg14</cparty>\n' \
        '</trade>\n' \
        '</NewTrade>'

fidstp_msg1 = '<NewTrade>\n' \
        '<id>5001</id>\n' \
        '<trade>\n' \
        '        <cparty>Morgan</cparty>\n' \
        '</trade>\n' \
        '</NewTrade>'
fidstp_msg2 = '<NewTrade>\n' \
        '<id>50023</id>\n' \
        '<trade>\n' \
        '        <cparty>Bloomberg</cparty>\n' \
        '</trade>\n' \
        '</NewTrade>'

icapture_trades = {
    '5001': icapture_msg1,
    '5002': icapture_msg2,
    '5003': icapture_msg3
}

fidstp_trades = {
    '5001': fidstp_msg1,
    '5002': fidstp_msg2,
}
