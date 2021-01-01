import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

columns_names = ['aah', 'aathi', 'abi', 'abiola', 'able', 'abt', 'abta', 'ac', 'acc', 'accept', 'access', 'accident', 'accidentally', 'accordingly', 'account', 'ache', 'across', 'action', 'activate', 'activity', 'actually', 'ad', 'add', 'added', 'addicted', 'addie', 'address', 'admirer', 'adore', 'adult', 'advance', 'advice', 'advise', 'ae', 'affair', 'affection', 'afraid', 'aft', 'afternoon', 'aftr', 'age', 'ago', 'ah', 'aha', 'ahead', 'ahmad', 'aight', 'aint', 'air', 'airport', 'aiya', 'aiyah', 'aiyar', 'aiyo', 'al', 'album', 'alcohol', 'alert', 'alex', 'alfie', 'alive', 'allah', 'almost', 'alone', 'along', 'already', 'alright', 'alrite', 'also', 'always', 'alwys', 'amazing', 'american', 'among', 'amount', 'amp', 'amt', 'an', 'angry', 'announcement', 'another', 'ansr', 'answer', 'answering', 'anti', 'anybody', 'anymore', 'anyone', 'anythin', 'anything', 'anytime', 'anyway', 'anyways', 'anywhere', 'apartment', 'apologise', 'app', 'apparently', 'apply', 'appointment', 'appreciate', 'apps', 'appt', 'april', 'ar', 'arcade', 'ard', 'area', 'argh', 'argue', 'argument', 'arm', 'armand', 'arng', 'around', 'arrange', 'arrested', 'arrive', 'arsenal', 'art', 'arun', 'as', 'asap', 'ask', 'askd', 'asked', 'askin', 'asking', 'asks', 'asleep', 'assume', 'ate', 'atlanta', 'atm', 'attempt', 'attend', 'auction', 'audition', 'august', 'aunt', 'aunty', 'auto', 'available', 'avatar', 'ave', 'avent', 'await', 'awaiting', 'awake', 'award', 'awarded', 'away', 'awesome', 'ba', 'babe', 'baby', 'back', 'bad', 'bag', 'bahamas', 'bak', 'balance', 'ball', 'bank', 'bar', 'barely', 'basic', 'basically', 'bat', 'bath', 'bathe', 'bathing', 'battery', 'bay', 'bb', 'bcm', 'bcoz', 'bcums', 'bday', 'bear', 'beautiful', 'beauty', 'become', 'becoz', 'bed', 'bedroom', 'beer', 'befor', 'begin', 'behave', 'behind', 'bein', 'believe', 'belive', 'bell', 'belly', 'belovd', 'ben', 'best', 'bet', 'better', 'beware', 'beyond', 'bf', 'bid', 'big', 'bigger', 'biggest', 'bill', 'billed', 'bin', 'bird', 'birla', 'birth', 'birthdate', 'birthday', 'bishan', 'bit', 'bitch', 'bite', 'biz', 'bk', 'black', 'blackberry', 'blah', 'blake', 'blame', 'blank', 'blanket', 'bleh', 'bless', 'blessed', 'blessing', 'blind', 'block', 'bloke', 'blonde', 'bloo', 'blood', 'bloody', 'bloomberg', 'blow', 'blu', 'blue', 'bluetooth', 'bluff', 'blur', 'bmw', 'boat', 'body', 'bold', 'bone', 'bonus', 'boo', 'book', 'booked', 'booking', 'boost', 'booty', 'bootydelious', 'bored', 'borin', 'boring', 'born', 'borrow', 'bos', 'boston', 'bother', 'bottle', 'bottom', 'bought', 'bout', 
                  'bowl', 'box', 'boy', 'boye', 'boyfriend', 'boytoy', 'bp', 'brah', 'brain', 'brand', 'brandy', 'bray', 'bread', 'break', 'breath', 'breathe', 'brief', 'bright', 'brilliant', 'bring', 'bringing', 'brings', 'bristol', 'british', 'britney', 'bro', 'broad', 'broke', 'bros', 'brothas', 'brother', 'brought', 'bslvyl', 'bstfrnd', 'bt', 'btw', 'buck', 'bud', 'budget', 'buff', 'bugis', 'building', 'bun', 'burger', 'burn', 'bus', 'business', 'busy', 'butt', 'buy', 'buying', 'buzy', 'buzz', 'bx', 'bye', 'cabin', 'cafe', 'cake', 'cal', 'calicut', 'california', 'call', 'callback', 'callcost', 'called', 'caller', 'callertune', 'callin', 'calling', 'cam', 'camcorder', 'came', 'camera', 'campus', 'cancel', 'cancer', 'cann', 'cannot', 'cant', 'captain', 'car', 'card', 'cardiff', 'care', 'career', 'careful', 'carefully', 'caring', 'carlos', 'carry', 'cartoon', 'case', 'cash', 'cat', 'catch', 'catching', 'caught', 'cause', 'cbe', 'cc', 'cd', 'celeb', 'celebrate', 'celebration', 'cell', 'center', 'centre', 'certainly', 'cha', 'chain', 'challenge', 'chance', 'change', 'changed', 'channel', 'character', 'charge', 'charged', 'charity', 'chart', 'chasing', 'chat', 'chatting', 'cheap', 'cheaper', 'chechi', 'check', 'checked', 'checking', 'cheer', 'chennai', 'chicken', 'chikku', 'child', 'childish', 'chill', 'chillin', 'china', 'chinese', 'choice', 'choose', 'chosen', 'christmas', 'church', 'cine', 'cinema', 'citizen', 'city', 'claim', 'claire', 'class', 'clean', 'cleaning', 'clear', 'cleared', 'click', 'clock', 'clos', 'close', 'closed', 'closer', 'club', 'cm', 'cn', 'co', 'cock', 'code', 'coffee', 'coin', 'cold', 'colleague', 'collect', 'collected', 'collecting', 'collection', 'college', 'colour', 'com', 'come', 'comedy', 'comin', 'coming', 'common', 'community', 'comp', 'company', 'competition', 'complete', 'completely', 'complimentary', 'computer', 'comuk', 'concentrate', 'concert', 'condition', 'confidence', 'confirm', 'confirmed', 'congrats', 'congratulation', 'connect', 'connection', 'considering', 'constantly', 'contact', 'contacted', 'content', 'contract', 'convey', 'cook', 'cooking', 'cool', 'copy', 'cornwall', 'correct', 'cost', 'costa', 'could', 'count', 'country', 'couple', 'course', 'cover', 'coz', 'cr', 'crab', 'crack', 'cramp', 'crave', 'crazy', 'cream', 'created', 'credit', 'credited', 'cross', 'croydon', 'cruise', 'cry', 'csbcm', 'cud', 'cuddle', 'cum', 'cup', 'current', 'currently', 'cust', 'custcare', 'customer', 'cut', 'cute', 'cutefrnd', 'cuz', 'cw', 'da', 'dad', 'daddy', 'dai', 'daily', 
                  'damn', 'dare', 'dark', 'darlin', 'darling', 'darren', 'dat', 'date', 'dating', 'dave', 'day', 'de', 'dead', 'deal', 'dear', 'dearer', 'dearly', 'death', 'december', 'decide', 'decided', 'decimal', 'decision', 'deep', 'def', 'definitely', 'del', 'deleted', 'deliver', 'delivered', 'deliveredtomorrow', 'delivery', 'dem', 'den', 'depends', 'derek', 'detail', 'dey', 'di', 'diamond', 'dick', 'dictionary', 'didnt', 'die', 'died', 'diet', 'diff', 'difference', 'different', 'difficult', 'dificult', 'digital', 'dignity', 'din', 'dinner', 'dint', 'direct', 'directly', 'dirty', 'dis', 'discount', 'discus', 'dislike', 'display', 'distance', 'disturb', 'division', 'divorce', 'diwali', 'dload', 'dnt', 'dobby', 'doc', 'dock', 'doctor', 'doesnt', 'dog', 'dogging', 'doggy', 'doin', 'dokey', 'doll', 'dollar', 'donate', 'done', 'donno', 'dont', 'door', 'dorm', 'dot', 'double', 'doubt', 'dough', 'download', 'downloaded', 'downloads', 'dr', 'dracula', 'draw', 'dream', 'dress', 'dressed', 'dresser', 'drink', 'drinkin', 'drinking', 'drive', 'drivin', 'driving', 'drms', 'drop', 'dropped', 'drove', 'drpd', 'drug', 'drunk', 'drunken', 'dry', 'dsn', 'dt', 'dubsack', 'duchess', 'dude', 'due', 'dumb', 'dun', 'dunno', 'durban', 'dvd', 'dx', 'ear', 'earlier', 'early', 'earn', 'earth', 'easier', 'easily', 'east', 'eastenders', 'easter', 'easy', 'eat', 'eaten', 'eatin', 'eating', 'ebay', 'ec', 'edge', 'edison', 'edu', 'educational', 'edward', 'ee', 'eek', 'eerie', 'effect', 'eg', 'egg', 'eh', 'eight', 'eighth', 'eire', 'either', 'ela', 'elaine', 'election', 'electricity', 'else', 'elsewhere', 'em', 'email', 'embarassed', 'empty', 'en', 'end', 'ended', 'ending', 'enemy', 'energy', 'eng', 'engin', 'england', 'english', 'enjoy', 'enjoyed', 'enjoyin', 'enough', 'enter', 'entered', 'entitled', 'entry', 'enuff', 'envelope', 'er', 'erm', 'error', 'escape', 'ese', 'especially', 'esplanade', 'essential', 'etc', 'euro', 'eve', 'even', 'evening', 'event', 'ever', 'every', 'everybody', 'everyone', 'everything', 'evn', 'evng', 'evry', 'ex', 'exact', 'exactly', 'exam', 'excellent', 'except', 'exciting', 'excuse', 'exe', 'executive', 'exhausted', 'expect', 'expecting', 'expensive', 'experience', 'expires', 'explain', 'express', 'extra', 'eye', 'fa', 'face', 'facebook', 'fact', 'failed', 'fair', 'fall', 'family', 'fan', 'fancy', 'fantastic', 'fantasy', 'far', 'farm', 'fast', 'faster', 'fat', 'father', 'fathima', 'fault', 'fave', 'favor', 'favour', 'favourite', 'fb', 'fear', 'feb', 'february', 'fee', 'feel', 'feelin', 'feeling', 
                  'fell', 'felt', 'female', 'fetch', 'fever', 'fifteen', 'fight', 'fighting', 'fightng', 'figure', 'file', 'fill', 'film', 'final', 'finally', 'find', 'fine', 'finger', 'finish', 'finished', 'finishing', 'fire', 'first', 'fish', 'fit', 'five', 'fix', 'fixed', 'fl', 'flag', 'flaked', 'flash', 'flat', 'flight', 'flirt', 'floor', 'flower', 'fly', 'fml', 'follow', 'followed', 'following', 'fone', 'food', 'fool', 'foot', 'football', 'footprint', 'force', 'foreign', 'forever', 'forevr', 'forget', 'forgot', 'form', 'forum', 'forward', 'forwarded', 'found', 'four', 'fr', 'fran', 'freak', 'free', 'freefone', 'freemsg', 'freephone', 'freezing', 'fren', 'frens', 'fri', 'friday', 'friend', 'friendship', 'frm', 'frnd', 'frnds', 'frndship', 'fromm', 'frying', 'fuck', 'fuckin', 'fucking', 'ful', 'full', 'fullonsms', 'fun', 'funny', 'furniture', 'future', 'fyi', 'ga', 'gal', 'game', 'gang', 'gap', 'garage', 'gardener', 'gary', 'gas', 'gautham', 'gave', 'gay', 'gb', 'gbp', 'gd', 'ge', 'gee', 'geeee', 'generally', 'gentle', 'gentleman', 'gently', 'genuine', 'germany', 'get', 'gettin', 'getting', 'getzed', 'gift', 'gimme', 'girl', 'girlfrnd', 'giv', 'give', 'given', 'giving', 'glad', 'gm', 'gn', 'go', 'goal', 'god', 'goin', 'going', 'gona', 'gone', 'gonna', 'good', 'goodmorning', 'goodnight', 'goodnite', 'google', 'gorgeous', 'gossip', 'got', 'goto', 'gotta', 'govt', 'gr', 'grahmbell', 'gram', 'grand', 'gravity', 'great', 'green', 'greet', 'greeting', 'grin', 'grl', 'ground', 'group', 'gt', 'guaranteed', 'gud', 'gudnite', 'guess', 'guide', 'guilty', 'guy', 'gym', 'ha', 'haf', 'haha', 'hahaha', 'hai', 'hair', 'haiz', 'half', 'halloween', 'ham', 'hand', 'handed', 'handle', 'handset', 'hanging', 'happen', 'happend', 'happened', 'happening', 'happens', 'happiness', 'happy', 'hard', 'hardcore', 'harry', 'hate', 'hav', 'havent', 'havin', 'havnt', 'head', 'headache', 'hear', 'heard', 'heart', 'heavy', 'hee', 'height', 'helen', 'hell', 'hella', 'hello', 'help', 'hey', 'hg', 'hi', 'hide', 'high', 'hill', 'hint', 'hip', 'history', 'hit', 'hiya', 'hl', 'hmm', 'hmmm', 'hmv', 'ho', 'hold', 'holder', 'holding', 'holiday', 'holla', 'hols', 'home', 'homeowner', 'hon', 'honey', 'honeybee', 'hook', 'hop', 'hope', 'hopefully', 'hoping', 'horny', 'horrible', 'hospital', 'hostel', 'hot', 'hotel', 'hour', 'house', 'however', 'hows', 'howz', 'hp', 'hr', 'http', 'hubby', 'hug', 'huh', 'hun', 'hundred', 'hungry', 'hunny', 'hurry', 'hurt', 'husband', 'hv', 'hw', 'iam', 'ibhltd', 'ibiza', 'ic', 'ice', 'id', 'idea', 'ideal', 
                  'identifier', 'idew', 'idiot', 'idk', 'ignore', 'ikea', 'il', 'ill', 'illness', 'im', 'image', 'imagine', 'imma', 'immediately', 'imp', 'impatient', 'important', 'impossible', 'improve', 'improved', 'inc', 'inch', 'incident', 'include', 'including', 'inclusive', 'inconsiderate', 'incredible', 'increment', 'indeed', 'index', 'india', 'indian', 'indicate', 'individual', 'indyarocks', 'infection', 'infernal', 'info', 'inform', 'information', 'informed', 'infront', 'ing', 'inning', 'innocent', 'inr', 'insha', 'inshah', 'inside', 'installing', 'instantly', 'instead', 'instituitions', 'instruction', 'insurance', 'intelligent', 'intention', 'interest', 'interested', 'interesting', 'interflora', 'internet', 'interview', 'intro', 'invader', 'invest', 'invite', 'invited', 'inviting', 'invnted', 'iouri', 'ip', 'ipad', 'ipod', 'iq', 'irritates', 'irritating', 'iscoming', 'ish', 'island', 'isnt', 'issue', 'italian', 'itcould', 'item', 'itwhichturnedinto', 'itz', 'ive', 'iz', 'izzit', 'ja', 'jacket', 'jackpot', 'jada', 'james', 'jamster', 'jan', 'jane', 'january', 'japanese', 'jas', 'jason', 'java', 'jay', 'jaya', 'jazz', 'jd', 'jealous', 'jean', 'jen', 'jenny', 'jerry', 'jess', 'jesus', 'jhl', 'jia', 'jiayin', 'jiu', 'jo', 'joanna', 'job', 'jogging', 'john', 'join', 'joined', 'joining', 'joke', 'jokin', 'joking', 'jolly', 'jolt', 'jordan', 'journey', 'joy', 'jsco', 'jst', 'jstfrnd', 'jsut', 'juan', 'juicy', 'july', 'june', 'jus', 'juz', 'kadeem', 'kaiez', 'kallis', 'kano', 'kappa', 'karaoke', 'kate', 'kavalan', 'kay', 'kb', 'ke', 'keep', 'keeping', 'kegger', 'kent', 'kept', 'kerala', 'keralacircle', 'kettoda', 'key', 'kg', 'kick', 'kickoff', 'kid', 'kidding', 'kidz', 'kill', 'killed', 'killing', 'kind', 'kinda', 'kindly', 'king', 'kiosk', 'kiss', 'kl', 'knackered', 'knee', 'knew', 'knock', 'know', 'knowing', 'knw', 'konw', 'kothi', 'kr', 'kudi', 'kusruthi', 'kz', 'la', 'lab', 'lac', 'lady', 'lag', 'laid', 'land', 'landline', 'lane', 'langport', 'language', 'laptop', 'lar', 'largest', 'last', 'late', 'lately', 'later', 'latest', 'latr', 'laugh', 'laughed', 'laughing', 'laundry', 'law', 'lay', 'lazy', 'lccltd', 'ldew', 'ldn', 'ldnw', 'le', 'lead', 'leaf', 'learn', 'least', 'leave', 'leaving', 'lect', 'lecture', 'left', 'leg', 'legal', 'leh', 'lei', 'lemme', 'length', 'leona', 'lesson', 'let', 'letter', 'lf', 'liao', 'lib', 'library', 'lick', 'lido', 'lie', 'life', 'lifetime', 'lifpartnr', 'lift', 'light', 'lik', 'like', 'liked', 'likely', 'lil', 'lily', 'limit', 'limiting', 'line', 'linerental',
                  'link', 'lion', 'lionm', 'lionp', 'lip', 'list', 'listen', 'listening', 'literally', 'little', 'live', 'lived', 'liverpool', 'living', 'lk', 'lmao', 'lo', 'load', 'loan', 'local', 'location', 'lock', 'log', 'login', 'logo', 'lol', 'london', 'lonely', 'long', 'longer', 'look', 'lookatme', 'looked', 'lookin', 'looking', 'loose', 'lor', 'lose', 'loses', 'losing', 'loss', 'lost', 'lot', 'lotr', 'lotta', 'lou', 'loud', 'lounge', 'lousy', 'lov', 'lovable', 'love', 'loved', 'lovejen', 'lovely', 'loveme', 'lover', 'loverboy', 'loving', 'lovingly', 'low', 'lower', 'loxahatchee', 'loyal', 'loyalty', 'lp', 'lst', 'lt', 'ltd', 'lttrs', 'luck', 'lucky', 'lucozade', 'lucy', 'lunch', 'lush', 'luv', 'luvs', 'lux', 'luxury', 'lv', 'lvblefrnd', 'lyf', 'lyfu', 'lyk', 'ma', 'maangalyam', 'mac', 'machan', 'macho', 'mad', 'madam', 'made', 'mag', 'maga', 'magical', 'mah', 'mahal', 'maid', 'mail', 'mailbox', 'main', 'maintain', 'major', 'make', 'makin', 'making', 'malaria', 'male', 'mall', 'man', 'manage', 'managed', 'management', 'manda', 'mandan', 'maneesha', 'many', 'map', 'march', 'margaret', 'mark', 'market', 'marriage', 'married', 'marrow', 'marry', 'massage', 'massive', 'master', 'match', 'mate', 'math', 'mathematics', 'matrix', 'matter', 'matured', 'maturity', 'max', 'maximize', 'may', 'mayb', 'maybe', 'mb', 'mca', 'mcat', 'meal', 'mean', 'meaning', 'meant', 'meanwhile', 'measure', 'med', 'medical', 'medicine', 'meet', 'meetin', 'meeting', 'mega', 'meh', 'mei', 'mel', 'melle', 'melt', 'member', 'membership', 'memory', 'men', 'mental', 'menu', 'meow', 'merry', 'mesages', 'mess', 'message', 'messaged', 'messaging', 'messenger', 'messy', 'met', 'mi', 'mid', 'middle', 'midnight', 'mids', 'might', 'mila', 'mile', 'milk', 'million', 'min', 'mind', 'mine', 'mini', 'minimum', 'minmobsmorelkpobox', 'minmoremobsemspobox', 'minnaminunginte', 'minor', 'minute', 'minuts', 'miracle', 'misbehaved', 'miserable', 'miss', 'missed', 'missin', 'missing', 'mistake', 'mite', 'mitsake', 'mix', 'mk', 'ml', 'mm', 'mmm', 'mmmm', 'mmmmm', 'mmmmmm', 'mnth', 'mnths', 'mo', 'moan', 'mob', 'mobile', 'mobilesdirect', 'mobilesvary', 'mobileupd', 'mobno', 'moby', 'mode', 'model', 'module', 'moji', 'mojibiola', 'mokka', 'mom', 'moment', 'mon', 'monday', 'money', 'monkey', 'mono', 'month', 'monthly', 'mood', 'moon', 'moral', 'morefrmmob', 'morn', 'mornin', 'morning', 'moro', 'morow', 'morphine', 'morro', 'morrow', 'mostly', 'mother', 'motorola', 'mountain', 'mouth', 'move', 'moved', 'movie', 'movietrivia', 'moving', 'mp', 'mr', 'mrng', 
                  'mrt', 'mrw', 'msg', 'msging', 'msgrcvd', 'msgrcvdhg', 'msn', 'mt', 'mtalk', 'mth', 'mths', 'mtmsg', 'mtmsgrcvd', 'mu', 'muah', 'much', 'mum', 'mummy', 'mumtaz', 'munsters', 'murder', 'murdered', 'murderer', 'music', 'must', 'musthu', 'muz', 'mystery', 'na', 'nag', 'nagar', 'nah', 'nahi', 'naked', 'nalla', 'name', 'named', 'nan', 'nanny', 'nap', 'nasdaq', 'nasty', 'nat', 'natalie', 'natalja', 'national', 'natural', 'nature', 'naughty', 'nb', 'nd', 'ne', 'near', 'nearly', 'necessarily', 'necessary', 'neck', 'necklace', 'ned', 'need', 'needed', 'neft', 'neighbor', 'neighbour', 'neither', 'nervous', 'net', 'netcollex', 'network', 'networking', 'neva', 'never', 'new', 'neway', 'newest', 'news', 'next', 'ni', 'nic', 'nice', 'nichols', 'nigeria', 'night', 'nimya', 'nit', 'nite', 'nitros', 'no', 'nobody', 'noe', 'nok', 'nokia', 'nokias', 'noline', 'none', 'noon', 'nope', 'norm', 'normal', 'normally', 'northampton', 'note', 'nothin', 'nothing', 'notice', 'notxt', 'noun', 'nowadays', 'nt', 'ntt', 'ntwk', 'nu', 'num', 'number', 'nurungu', 'nuther', 'nvm', 'nw', 'nxt', 'ny', 'nyc', 'nydc', 'nyt', 'obviously', 'occupy', 'odi', 'offer', 'office', 'official', 'officially', 'ofice', 'often', 'oh', 'oi', 'oic', 'oil', 'ok', 'okay', 'okey', 'okie', 'ola', 'old', 'omg', 'omw', 'one', 'oni', 'onion', 'online', 'onto', 'onwards', 'oooh', 'oops', 'open', 'opening', 'operator', 'opinion', 'opportunity', 'opt', 'option', 'optout', 'orange', 'orchard', 'order', 'ordered', 'oredi', 'oreo', 'orig', 'original', 'oru', 'oso', 'others', 'otherwise', 'otside', 'outage', 'outside', 'outstanding', 'outta', 'ovulation', 'ow', 'owns', 'oz', 'pa', 'pack', 'package', 'page', 'paid', 'pain', 'painful', 'painting', 'pale', 'pan', 'pandy', 'panic', 'pap', 'paper', 'paperwork', 'paragon', 'parco', 'parent', 'paris', 'park', 'parked', 'parking', 'part', 'partner', 'partnership', 'party', 'pas', 'passed', 'passionate', 'password', 'past', 'path', 'pattern', 'patty', 'pay', 'payed', 'payee', 'paying', 'payment', 'payoh', 'pc', 'peace', 'peaceful', 'peak', 'pee', 'pen', 'pending', 'penis', 'penny', 'people', 'per', 'percent', 'perfect', 'perhaps', 'period', 'permission', 'person', 'personal', 'personality', 'perwksub', 'pete', 'petey', 'petrol', 'pg', 'ph', 'philosophy', 'phne', 'phoenix', 'phone', 'phoned', 'photo', 'php', 'pic', 'pick', 'picked', 'picking', 'pickle', 'picsfree', 'picture', 'pie', 'piece', 'pig', 'pilate', 'pimple', 'pin', 'pink', 'piss', 'pissed', 'pix', 'pizza', 'place', 'placement', 'plan', 'plane', 'planet', 
                  'planned', 'planning', 'play', 'played', 'player', 'playing', 'plaza', 'please', 'pleased', 'pleasure', 'plenty', 'plm', 'pls', 'plus', 'plz', 'pm', 'po', 'pobox', 'pocketbabe', 'pod', 'poem', 'point', 'poker', 'pole', 'police', 'politician', 'polo', 'poly', 'polyh', 'polyph', 'polyphonic', 'polys', 'pongal', 'pool', 'poop', 'poor', 'pop', 'popcorn', 'popped', 'porn', 'position', 'possession', 'possible', 'post', 'postcard', 'postcode', 'posted', 'potato', 'potential', 'potter', 'pouch', 'pound', 'pours', 'pout', 'power', 'pp', 'ppermesssubscription', 'ppl', 'pple', 'ppm', 'ppmx', 'ppw', 'prabha', 'practical', 'practice', 'practicing', 'pray', 'praying', 'pre', 'prefer', 'preferably', 'prem', 'premier', 'premium', 'prepaid', 'prepare', 'prepared', 'prepayment', 'prescription', 'present', 'press', 'pretty', 'previous', 'previously', 'prey', 'price', 'pride', 'prince', 'princess', 'print', 'printed', 'priscilla', 'privacy', 'private', 'prize', 'pro', 'prob', 'probably', 'problem', 'probs', 'process', 'processed', 'prof', 'professor', 'profile', 'profit', 'program', 'project', 'prolly', 'promise', 'promo', 'prompt', 'proof', 'properly', 'property', 'propose', 'propsd', 'prospect', 'protect', 'prove', 'proverb', 'provided', 'pt', 'ptbo', 'pub', 'public', 'pull', 'purchase', 'purity', 'purpose', 'purse', 'push', 'pussy', 'put', 'puttin', 'putting', 'pw', 'px', 'qatar', 'qp', 'qu', 'quality', 'queen', 'ques', 'question', 'questioned', 'quick', 'quickly', 'quiet', 'quit', 'quite', 'quiz', 'quote', 'quoting', 'qxj', 'racing', 'radio', 'raed', 'rael', 'railway', 'rain', 'raining', 'raise', 'raj', 'raji', 'rakhesh', 'rally', 'ran', 'random', 'randomly', 'randy', 'rang', 'range', 'ranjith', 'rate', 'rather', 'ray', 'rcv', 'rcvd', 'rd', 'reach', 'reached', 'reaching', 'reaction', 'read', 'reader', 'reading', 'ready', 'real', 'realise', 'reality', 'realize', 'realized', 'really', 'realy', 'reason', 'reasonable', 'reboot', 'rec', 'recd', 'receipt', 'receive', 'receivea', 'received', 'receiving', 'recent', 'recently', 'recession', 'recharge', 'reckon', 'recognise', 'record', 'recovery', 'red', 'redeemed', 'reduce', 'ref', 'reference', 'refilled', 'refused', 'reg', 'regard', 'regarding', 'register', 'registered', 'regret', 'regular', 'relation', 'relative', 'relax', 'released', 'rem', 'remain', 'remains', 'remember', 'remembered', 'remembr', 'remind', 'reminder', 'reminding', 'removal', 'remove', 'removed', 'renewal', 'rent', 'rental', 'rentl', 'repair', 'repeat', 'replace', 'replacement', 'replied',
                  'reply', 'replying', 'report', 'representative', 'request', 'research', 'reserve', 'respect', 'respectful', 'responce', 'respond', 'responding', 'response', 'responsibility', 'rest', 'restaurant', 'result', 'resume', 'retrieve', 'return', 'returned', 'reveal', 'revealed', 'reverse', 'review', 'revision', 'reward', 'rewarding', 'rg', 'rgds', 'rhythm', 'rice', 'rich', 'ride', 'right', 'rightly', 'ring', 'ringtone', 'ringtoneking', 'ringtones', 'risk', 'rite', 'river', 'road', 'roast', 'rock', 'rofl', 'roger', 'role', 'romantic', 'ron', 'room', 'roommate', 'rose', 'round', 'row', 'royal', 'rply', 'rr', 'rstm', 'ru', 'rub', 'rude', 'ruin', 'ruining', 'rule', 'rum', 'rumour', 'run', 'running', 'rush', 'rw', 'ryan', 'sac', 'sachin', 'sacrifice', 'sad', 'sae', 'safe', 'said', 'sake', 'salam', 'salary', 'sale', 'salon', 'sam', 'santa', 'sar', 'sarasota', 'sarcasm', 'sarcastic', 'sary', 'sat', 'sathya', 'satisfied', 'satisfy', 'saturday', 'saucy', 'savamob', 'save', 'saved', 'saw', 'say', 'saying', 'scared', 'scary', 'sch', 'schedule', 'school', 'science', 'scold', 'score', 'scoring', 'scotch', 'scotland', 'scotsman', 'scream', 'screamed', 'screaming', 'screen', 'scrounge', 'sd', 'se', 'sea', 'search', 'searching', 'season', 'seat', 'sec', 'second', 'secret', 'secretary', 'secretly', 'section', 'sed', 'see', 'seed', 'seeing', 'seem', 'seemed', 'seems', 'seen', 'select', 'selected', 'selection', 'self', 'selfish', 'sell', 'selling', 'sem', 'semester', 'sen', 'send', 'sender', 'sending', 'sends', 'sense', 'sensitive', 'sent', 'sentence', 'senthil', 'sept', 'series', 'serious', 'seriously', 'service', 'serving', 'set', 'setting', 'settle', 'settled', 'seven', 'several', 'sex', 'sexy', 'sh', 'sha', 'shagged', 'shahjahan', 'shall', 'shame', 'shampain', 'share', 'shared', 'sharing', 'shd', 'sheet', 'sheffield', 'shelf', 'shesil', 'shijas', 'shining', 'ship', 'shipped', 'shipping', 'shirt', 'shit', 'shitload', 'shld', 'shock', 'shocking', 'shoe', 'shoot', 'shop', 'shoppin', 'shopping', 'shore', 'short', 'shortage', 'shorter', 'shortly', 'shot', 'shouted', 'shoving', 'show', 'shower', 'showing', 'shracomorsglsuplt', 'shu', 'shuhui', 'shut', 'shy', 'si', 'sian', 'sib', 'sick', 'side', 'sigh', 'sight', 'sign', 'signing', 'silence', 'silent', 'silently', 'silver', 'sim', 'simple', 'simpler', 'simply', 'since', 'sinco', 'sing', 'singing', 'single', 'sip', 'sipix', 'sir', 'sister', 'sit', 'site', 'sitll', 'sitting', 'situation', 'siva', 'six', 'size', 'sk', 'skilgme', 'skillgame', 'skip', 'sky', 'skype',
                  'skyped', 'slap', 'slave', 'sleep', 'sleepin', 'sleeping', 'sleepwell', 'sleepy', 'slept', 'slice', 'slide', 'slightly', 'slip', 'slipper', 'slo', 'slot', 'slow', 'slowly', 'slp', 'sm', 'small', 'smart', 'smashed', 'smell', 'smeone', 'smile', 'smiling', 'smith', 'smoke', 'smoking', 'smsco', 'smth', 'sn', 'snake', 'snogs', 'snow', 'snowman', 'social', 'sofa', 'soft', 'software', 'soiree', 'sol', 'solve', 'solved', 'somebody', 'someone', 'somethin', 'something', 'sometime', 'sometimes', 'somewhere', 'song', 'sony', 'sonyericsson', 'soon', 'sooner', 'sore', 'sorrow', 'sorry', 'sort', 'sorted', 'sorting', 'sory', 'soryda', 'sound', 'soup', 'source', 'south', 'sp', 'space', 'spanish', 'spare', 'speak', 'special', 'specially', 'speechless', 'speed', 'spell', 'spend', 'spending', 'spent', 'spk', 'spl', 'spoke', 'spoken', 'spook', 'sport', 'spree', 'spring', 'sry', 'st', 'staff', 'stamp', 'stand', 'standard', 'standing', 'star', 'start', 'started', 'starting', 'starwars', 'statement', 'station', 'stay', 'staying', 'std', 'step', 'still', 'stock', 'stockport', 'stomach', 'stomp', 'stone', 'stop', 'stopped', 'stoptxt', 'store', 'storming', 'story', 'str', 'straight', 'stranger', 'street', 'stress', 'strike', 'strong', 'stuck', 'student', 'study', 'studying', 'stuff', 'stupid', 'style', 'stylish', 'sub', 'subpoly', 'subscribe', 'subscribed', 'subscriber', 'subscription', 'successful', 'successfully', 'suck', 'sugar', 'suggest', 'suite', 'sum', 'summer', 'sun', 'sunday', 'sunny', 'sunshine', 'suntec', 'sup', 'super', 'supervisor', 'supply', 'support', 'supposed', 'suprman', 'sura', 'sure', 'surely', 'surfing', 'surprise', 'surprised', 'sw', 'sweet', 'sweetest', 'swimming', 'swing', 'switch', 'swt', 'swtheart', 'symbol', 'system', 'ta', 'table', 'tablet', 'take', 'taken', 'takin', 'taking', 'talent', 'talk', 'talking', 'tampa', 'tape', 'tariff', 'tat', 'taunton', 'taylor', 'tb', 'tc', 'tcr', 'tea', 'teach', 'teacher', 'team', 'tear', 'tease', 'teasing', 'technical', 'teeth', 'tel', 'tell', 'telling', 'telphone', 'temp', 'temple', 'ten', 'tenant', 'tenerife', 'term', 'terrible', 'tessy', 'test', 'text', 'textbuddy', 'textcomp', 'texted', 'texting', 'textoperator', 'textpod', 'tf', 'tg', 'th', 'thangam', 'thank', 'thanks', 'thanksgiving', 'thanx', 'thats', 'theatre', 'themob', 'theory', 'there', 'thesis', 'thgt', 'thing', 'think', 'thinkin', 'thinking', 'thk', 'thm', 'thnk', 'tho', 'thot', 'though', 'thought', 'thousand', 'thread', 'threat', 'three', 'threw', 'throat', 'throw', 'thru', 'tht', 'thts',
                  'thurs', 'thursday', 'thx', 'thy', 'ti', 'tick', 'ticket', 'tight', 'tihs', 'til', 'till', 'time', 'timing', 'tip', 'tired', 'tirunelvali', 'tirupur', 'tissco', 'title', 'tiwary', 'tkts', 'tlk', 'tlp', 'tm', 'tmr', 'tncs', 'toa', 'toclaim', 'today', 'tog', 'together', 'told', 'toll', 'tom', 'tomarrow', 'tomo', 'tomorrow', 'tone', 'tonight', 'tonite', 'took', 'top', 'torch', 'tot', 'total', 'totally', 'touch', 'touched', 'tough', 'tour', 'towards', 'town', 'track', 'train', 'training', 'transaction', 'transfer', 'transfered', 'travel', 'treat', 'tree', 'tried', 'trip', 'trouble', 'true', 'truly', 'trust', 'truth', 'try', 'trying', 'tscs', 'tsunami', 'tt', 'ttyl', 'tuesday', 'tuition', 'turn', 'tv', 'twelve', 'twice', 'two', 'txt', 'txtauction', 'txtin', 'txting', 'txts', 'tyler', 'type', 'tyrone', 'ubi', 'ugh', 'uk', 'umma', 'ummmmmaah', 'un', 'unable', 'uncle', 'understand', 'understanding', 'understood', 'uni', 'unique', 'university', 'unless', 'unlimited', 'unredeemed', 'unsold', 'unsub', 'unsubscribe', 'update', 'upgrade', 'upload', 'upset', 'upto', 'ur', 'urawinner', 'ure', 'urgent', 'urgently', 'urgnt', 'url', 'urn', 'urself', 'usc', 'use', 'used', 'user', 'usf', 'using', 'usual', 'usually', 'uz', 'valentine', 'valid', 'valuable', 'value', 'valued', 'various', 'vary', 'vava', 'vegetable', 'verify', 'version', 'vettam', 'via', 'video', 'videochat', 'videophones', 'vijay', 'vikky', 'village', 'violence', 'vip', 'virgin', 'visit', 'vl', 'voda', 'vodafone', 'vodka', 'voice', 'voicemail', 'vomit', 'vote', 'voucher', 'vry', 'wa', 'wah', 'waheed', 'waht', 'wait', 'waited', 'waitin', 'waiting', 'wake', 'waking', 'wale', 'walk', 'walked', 'walking', 'wall', 'wallpaper', 'walmart', 'wan', 'wana', 'wanna', 'want', 'wanted', 'wanting', 'wap', 'warm', 'warner', 'warning', 'warranty', 'waste', 'wasted', 'wat', 'watch', 'watching', 'water', 'watever', 'wating', 'wats', 'wave', 'way', 'wb', 'wc', 'weak', 'wear', 'wearing', 'weather', 'web', 'website', 'wed', 'wedding', 'wednesday', 'weed', 'week', 'weekend', 'weekly', 'weight', 'weird', 'welcome', 'well', 'welp', 'wen', 'went', 'wer', 'wet', 'whatever', 'whats', 'whenever', 'whenevr', 'wherever', 'whether', 'white', 'who', 'whole', 'wid', 'wif', 'wife', 'wil', 'willing', 'win', 'winaweek', 'winawk', 'wind', 'window', 'wine', 'winner', 'winning', 'wisdom', 'wise', 'wish', 'wishing', 'wit', 'within', 'without', 'wiv', 'wk', 'wkend', 'wkg', 'wkly', 'wks', 'wn', 'wnt', 'woke', 'woman', 'wonder', 'wonderful', 'wondering', 'wont', 'word', 'work', 'workin',
                  'working', 'world', 'worried', 'worry', 'worse', 'worth', 'wot', 'would', 'wow', 'wp', 'wq', 'wrc', 'write', 'wrk', 'wrong', 'wt', 'wtf', 'wu', 'wud', 'wun', 'www', 'wx', 'wylie', 'xavier', 'xchat', 'xh', 'xmas', 'xuhui', 'xx', 'xxx', 'xxxx', 'xxxxxxx', 'xxxxxxxxx', 'xy', 'ya', 'yahoo', 'yan', 'yar', 'yay', 'yeah', 'year', 'yeh', 'yep', 'yer', 'yes', 'yest', 'yesterday', 'yet', 'yetunde', 'yijue', 'ym', 'yo', 'yoga', 'yogasana', 'yor', 'yr', 'yummy', 'yun', 'yuo', 'yup', 'zed']

                  
                 
def input_process(message: str) -> str:

    wordnet = WordNetLemmatizer()
    capturing_words = re.sub('[^a-zA-Z]', ' ', message)
    lowering_spliting = capturing_words.lower().split()
    rm_unwanted_words = [wordnet.lemmatize(word) for word in lowering_spliting
                            if not word in set(stopwords.words('english'))]
    finalized_word = ' '.join(rm_unwanted_words)

    return finalized_word

  
def proceess_message(message: str) -> str:
    
    message = input_process(message)
    dummy_list = [0 for _ in range(3000)]
    for i in message.split():
      if i in columns_names:
        temp = columns_names.index(i)
        if dummy_list[temp] >= 1:
          dummy_list[temp] += 1
        else:
          dummy_list[temp] = 1
          
    return dummy_list
    
    
    
    
    
    
    
