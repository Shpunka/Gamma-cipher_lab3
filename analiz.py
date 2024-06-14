def coincidence_index(text, key_length):
    letters = [char.lower() for char in text if char.isalpha()]
    counts = {}

    for i in range(len(letters)):
        if i % key_length == 0:
            char = letters[i]
            counts[char] = counts.get(char, 0) + 1

    total_chars = sum(counts.values())
    if total_chars <= 1:
        return 0

    index = sum(count * (count - 1) for count in counts.values()) / (total_chars * (total_chars - 1))
    return index


text = input("Enter a text to calculate coincidence index: ")
for key in range(1, 5):
    print(f'Индекс совпадений при ключе {key}: {coincidence_index(text, key)}')


text = "lzuyszrvkodvhcvosclhnwvklfwxsywwuqggqrzdgqvwzlgsbuudzzragnserixowlhsgvwkuotgauusirbbhbohbzszkdgkgctrhnhgowozhhudgqpslrfgvgovhgqqklosdzcdmyksxhhuvivscxwmuxwtdbezoewvgwwidbzkotnmuxtuuiylbmpmyhfblqkvwgsdxhqodhkwvkrdvrfzxbowmzrvkoderindjkduxhozgoedvkdrgqrxhakppkuwgpxavhgpsyvomhocdmcksthjkumuxbkhrshmuxfydhovtgfhorbovaewcvsforfowmgqrozwroruhjkumzkwtjwidbzrdxrjogsericlhnwvkesywduvgoezkdgylgzdbihotgualrgqqklosfctvhgqhrbzkdftlbmdbjlavucblbmwchhhzhfyhfbhmuxpkfoavsowfaomidfkdpuxherixzsrohhwtjotgvgsdoqsyvwbdzahhnhhxxgzbcakobhdrdqkgwtpsgqrozwrokuuyndfjwckaqkhrerixhlvhqzdhorbyhjkumzlakbcalbzhfgfhclhnpszkotnmuxtuupklbmdjgoikgiyhfgqrlrfgozuzwtjakwchhovdfzrterixowlhwrrcqicxzoxghudgylgzlbmbcalbgqmcdmzkozlqgqotghupoqlbmbcausdssxlstfsclhnpsvrgowwbhotgdxrrafhoysoimuxvgysgqmlhsjeoincxvimjsywwuqgvosgvsrhhshytrkyrhndhofotfctwwtxszrwssfuysgqrjhzoysxwvkesywgkujofsvrgylprhmuxfoqdawwylavrfzdbzwcshotgwcdbzwckqgauszkozlospskwwtjmuxfthsjvotgsdssiwozlctvhndbqbcaicxwoqlbmwvkwwshhufcspitlqgwsclhnpsodanhfkwcrlgzhbgqrzrvkoderigfvohjkviifsyvotgvgsdoqsyvwgpuxdhkiiricxwvkrdvrfzxbowmzrpkrtyhfblqkwcerigqrozwroorzoevgzuwbhhuesgusrlohosgqrkitkfhoysgvgovhgqhlrfgozerixqskggxhakppkuhndhodanhfkicxbcazvkqsbhferithsjpsgqrzkozlosgsjlqgwsjwcvucblroquericlhnwvkesywduvgoezkvivscxwotgualrgqqklovsfkfwgwserixwfavhoqakdbjlosfctiwjhbzwvgwwidbnhzvbcausgfverixjcgoggqryrzbhmuxfvuchossvwgpqupaowhkghubcauggwwyioiwwuqotgwclzrjcgecbhotgpkbctghuhbyxfkwvgwmuxoxhvgsdezwzkhnhoyvwywotfsosfuywjhmuxqgqquxbzrbshhueszksxhtuumuxknhbkysxbcaqskgaklosksxhhupoqhmuxfrltkhoylsxdbjwcyxdvrfzbcalbgqmcdmzkozlqgqwgpmuxfvhfyrbgooyvwywotwotgwgpozbcaugkujofsrhhshytrknrkofotksrsmuxhugoedbjlkoozjraeesywhudgylgzbcazwzkotbhnlbmbcaqskgxavhgvygqrozwropkksxhhusfuywjhmuxkowvzksyxdvrfzdbjjiogotfserigusrrcqlbmicxlosgsjlqgwsjwcsdyoquerixhlvhfohbihkowvshduvwzljkdbjsfugiiwwbhguszkdgkgctrhnhgowozhhuusgfvuxhzrakzvkqsbhferithsjdgylgzdbihwgpvkuslrferigqrozwroorzoevrupmhhgzwcnhzvbcadqnlsbhmuxfmrorvotgcbhfirakdberpywoiosybcapoeioihwgpmuxfgozedbjlkoozyxdvrfzbcalbkysxbkgbduvgoezkvczkozbcafotviifskgotghnuwbhwgpvkuszragnserixowlhsgvwkuotghuksrsmuxbgywmdhkdbefvgozkqukvhndhirakbcaukgbhujszksxzsidbgfqupdrlgnjfkdhzkwtjgyrzkwiyzcxnhujszksxwcgfvohjkbcaurxhosvotgoyswxdhorbylosksxhhuvivscxwmuxotghusfuywjhmuxkowvzkszrcrvotgfkvcauqkvmuxbkhrzrgafqkhrzkotnmuxtuuhxxgzlbmpszrpkbcauoyvwywotwwgpvuqcxhrzrpkddguhuimuxfrltkdbjlkoozgokgbghhvkuslrferioddvusilozhmuxfrrmgohedbjlzurylrfcdfjwcnhzvlbmbcalbgqmcdmzkozlqgqagbsbhfegoeesgjfkdhuqslrferigqrsdmerillbjviifsyvotgvgsdoqsyvwtdzrwvgwmuxrulosksxhhudgylgzbcarberixmcaubkbhujfkdhthgydbjlkoozjrsbhfewvoquoqaescchfzrvkoderixhoikmuxflxzrsczhbzlorwvgqyerilrfikcuvwtjakdgerixdgylgzdbzlkoozgokgbghhvkuszrgasduuherigqrzrualrkbcawcyxqihgylovsfkfwgwserixwfavhoqakdbjlkoozgokgbgcrfqkoxghuhoxqwzwvgqyerilrfhhwtjobdzahravsxlosksxhtuumuxknhbkysxbcaqskgakdbjlkoozgokgbgjraeesywhuksrsmuxwtdbezoewvgwwidberixvozlgldqzlctlgopduuhgqhzrakdbjlkoozmrohrjkdbjeserbjwckqgauszkozbcadfkkovsmclhnwvkdgylgzdbihwvucblrkwvgqyerilrfavwtjaevsxywihgodamuozhtaotuuhnhcvscxwitlhewcgvgovherigqrozwroorzoevgzuwbhhuesgusrlohosgqrkitkfhoysgvgovhgqhlrfgozerixqskggodajhrofozhrzrmuxfydhovtgfhorbgqrozwroruhjkumzkwtjwidbzrdxrjogsericlhnwvkesywduvgoezkvivscxwotgualrgqqkwvgqyerilrfgozuzwtjakwchhovdfzrterixowlhwgpdxljoosmhrzrpkbcauoyvwywotwotgwclzrdzcdmyesnhf"

def cryptoanaliz(text: str, key_length: int):
    l = key_length
    groups_1 = [text[i:i + l:l] for i in range(0, len(text), l)]
    groups_2 = [text[i + 1:i + l + 1:l] for i in range(0, len(text), l)]
    groups_3 = [text[i + 2:i + l + 2:l] for i in range(0, len(text), l)]
    result_1 = ' '.join(groups_1)
    result_2 = ' '.join(groups_2)
    result_3 = ' '.join(groups_3)
    return result_1[:12], result_2[:12], result_3[:12]

def caesar_decrypt(word, shift):
    decrypted_word = ""
    for char in word:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_word += chr(shifted)
        else:
            decrypted_word += char
    return decrypted_word

groups = cryptoanaliz(text, 3)

length = min(len(group) for group in groups)

for shift1 in range(26):
    for shift2 in range(26):
        for shift3 in range(26):
            decrypted_text = ""
            for i in range(length):
                decrypted_text += caesar_decrypt(groups[0][i], shift1).strip() + caesar_decrypt(groups[1][i], shift2).strip() + caesar_decrypt(groups[2][i], shift3).strip()
            decrypted_text += '\n'

            print(f"Shifts: {shift1}, {shift2}, {shift3}")
            print(decrypted_text)

