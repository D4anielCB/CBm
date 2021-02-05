# -*- coding: utf-8 -*-
import urllib, urlparse, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, hashlib, re, urllib2, htmlentitydefs, unicodedata, math, xbmcvfs
import shutil
from metahandler import metahandlers
from metadatautils import MetadataUtils

AddonID = 'plugin.video.CubePlayMeta'
Addon = xbmcaddon.Addon(AddonID)
AddonName = Addon.getAddonInfo("name")
icon = Addon.getAddonInfo('icon')

addonDir = Addon.getAddonInfo('path').decode("utf-8")
iconsDir = os.path.join(addonDir, "resources", "images")

libDir = os.path.join(addonDir, 'resources', 'lib')
sys.path.insert(0, libDir)
import common

addon_data_dir = xbmc.translatePath(Addon.getAddonInfo("profile")).decode("utf-8")
cacheDir = os.path.join(addon_data_dir, "cache")
if not os.path.exists(cacheDir):
	os.makedirs(cacheDir)

cFonte1 = Addon.getSetting("cFonte1")
cFonte2 = Addon.getSetting("cFonte2")
cFonte3 = Addon.getSetting("cFonte3")

cTxt1 = Addon.getSetting("cTxt1")
cTxt2 = Addon.getSetting("cTxt2")
cTxt3 = Addon.getSetting("cTxt3")

DirM = Addon.getSetting("cDir")
DirB = Addon.getSetting("cDirB")
CEle = Addon.getSetting("cEle")

DirCount = Addon.getSetting("DirCount") if Addon.getSetting("DirCount") != "" else 0

MUlang = "pt-BR" if Addon.getSetting("MUlang") == "0" else "en"
MUcache = True if Addon.getSetting("MUcache") == "true" else False
MUcacheEpi = True if Addon.getSetting("MUcacheEpi") == "true" else False

Cat = Addon.getSetting("Cat") if Addon.getSetting("Cat") != "" else 0
Cat2 = Addon.getSetting("Cat2") if Addon.getSetting("Cat2") != "" else "0"
Cidi = Addon.getSetting("Cidi") if Addon.getSetting("Cidi") != "" else "0"
Ctrakt = Addon.getSetting("Ctrakt") if Addon.getSetting("Ctrakt") != "" else None
Clista=["Sem filtro (Mostrar Todos)","Ação", "Animação", "Aventura", "Crime", "Comédia", "Documentário", "Drama", "Fantasia", "Ficção científica", "Mistério", "Romance", "Terror", 'Thriller']
CImdb=["nome","ano","vote"]
CImdb2=["Nome","Ano","Rating"]

proxy = "http://cubeplay.000webhostapp.com/nc/nc.php?u="
proxy = ""

RC="redecanais.cloud/"
RCref="https://gamesgo.fun/"

def setViewS():
	xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
	xbmc.executebuiltin("Container.SetViewMode(50)")
def setViewS2():
	xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')	
	xbmc.executebuiltin("Container.SetViewMode(55)")
def setViewM():
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
def setViewM2():
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(50)")
	
def getLocaleString(id):
	return Addon.getLocalizedString(id).encode('utf-8')

def Categories(): #70
	#AddDir("[COLOR green][B][Superflix][/B][/COLOR]" , "http://www.superflix.net/assistir-the-good-doctor-online-dublado-legendado-hd-11/", 402, "https://accelerator-origin.kkomando.com/wp-content/uploads/2015/04/update2-970x546.jpg", "https://accelerator-origin.kkomando.com/wp-content/uploads/2015/04/update2-970x546.jpg", isFolder=True)
	#AddDir("a","/the-beach-bum-dublado-2019-720p_299813944.html", 96, "", "", isFolder=False, IsPlayable=True)
	if len(DirM) > 7:
		AddDir("[COLOR maroon][B][Baixar][/B][/COLOR]" , "", 302, "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg")
		AddDir("[COLOR blue][B][Latest][/B][/COLOR]" , "", 300, "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg")
		AddDir("Next Episodes" , "", 308, isFolder=True)
		#AddDir("[COLOR blue][B][All][/B][/COLOR]" , "", 301, "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg")
	try:
		info2=""
		"""link = common.OpenURL("http://netcine.me/tvshows/page/1/").replace('\n','').replace('\r','')
		l2 = re.compile("box_movies(.+)").findall(link)
		lista = re.compile("img src\=\"[^\"]+.+?alt\=\"([^\"]+)").findall(l2[0])
		for x in lista:
			info2+=x.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'")+"\n" """
	except:
		info2=""
	if cTxt1 and cFonte1:
		AddDir("[COLOR white][B]["+cTxt1+"][/B][/COLOR]" , "", 51, "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg", info=info2)
	if cTxt2 and cFonte2:
		AddDir("[COLOR white][B]["+cTxt2+"][/B][/COLOR]" , "", 52, "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg", info=info2)
	if cTxt3 and cFonte3:
		AddDir("[COLOR white][B]["+cTxt3+"][/B][/COLOR]" , "", 53, "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg", info=info2)
	AddDir("[COLOR white][B][Animes][/B][/COLOR]", "" ,500 , "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg")
	AddDir("[COLOR orange][B][Clean Cache][/B][/COLOR]", "" ,666 , "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False)
	if len(DirM) > 7:
		AddDir("[COLOR green][B][Filmes Fav][/B][/COLOR]", "" ,352 , "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg")
		AddDir("[COLOR blue][B][Filmes][/B][/COLOR]", "" ,353 , "", "https://ckneiferinstructional.files.wordpress.com/2010/12/tv-shows-completed1.jpg")
	AddDir("[COLOR orange][B][Atualizar][/B][/COLOR]" , "", 200, "https://accelerator-origin.kkomando.com/wp-content/uploads/2015/04/update2-970x546.jpg", "https://accelerator-origin.kkomando.com/wp-content/uploads/2015/04/update2-970x546.jpg", isFolder=False)
	AddDir("[COLOR maroon][B][Atualizar Biblioteca][/B][/COLOR]" , "", 101, "https://accelerator-origin.kkomando.com/wp-content/uploads/2015/04/update2-970x546.jpg", "https://accelerator-origin.kkomando.com/wp-content/uploads/2015/04/update2-970x546.jpg", isFolder=False)
# --------------  Animes
def playanimenextvis(): #504
	try:
		trak = traktS()
		link = common.OpenURL(url)
		lista = re.compile("[^']+\/download").findall(link)
		E = 1
		i = re.compile('i\=(\d+)').findall(url)
		if i:
			E = int(i[0])
		totalepi = str( len(lista)+E-1 )
		meta = eval(metah)
		for l in lista:
			pc = 1 if meta['imdb_id']+str(meta['season_number'])+str(int(E)) in trak else None
			if pc == None:
				global url, episode, background, playcount
				playcount = pc
				episode = str(E)
				url = l
				NF( "Epi. "+str(E)+"/"+ totalepi )
				playanimevisauto()
				return
				sys.exit()
			E = E + 1
	except:
		sys.exit()
	NF("Temporada Completa")
	sys.exit()
def listanimevis(): #500
	try:
		link = common.OpenURL("https://pastebin.com/raw/nrC8aGLT").replace("\n","+")
		lista = re.compile("\*?(.+?);(\d+)?;\+(.+?)\*").findall(link)
		lista = sorted(lista, key=lambda lista: lista[0])
		for name2,id2,cont in lista:
			try:
				mg = MetadataUtils()
				mmm = mg.get_tvshow_details(title=name2,tmdb_id=id2, ignore_cache=MUcache, lang=MUlang)
				dubleg="[COLOR yellow][D][/COLOR]" if "dublado" in cont else "[COLOR blue][L][/COLOR]"
				AddDir2(dubleg+" "+mmm[-1]["TVShowTitle"].encode('utf-8'), id2, 501, iconimage, iconimage, info="", isFolder=True, background=background, metah=mmm[-1])
			except:
				pass
	except:
		pass
	return
def listseavis(): #501
	link = common.OpenURL("https://pastebin.com/raw/nrC8aGLT").replace("\n","+")
	lista = re.compile("\*?(.+?);(\d+)?;\+(.+?)\*").findall(link)
	lista = sorted(lista, key=lambda lista: lista[0])
	for name2,id2,cont2 in lista:
		if id2 == url:
			cont1 = cont2
	lista = re.compile("(\d+);(.+?)\+").findall(cont1)
	for season,url2 in lista:
		try:
			meta = eval(metah)
			mg = MetadataUtils()
			mmm = mg.get_tvshow_details(title="",tmdb_id=meta['tmdb_id'], ignore_cache=MUcache, lang=MUlang)
			metasea=mergedicts(meta,mmm[int(season)])
			dubleg="[COLOR yellow][D][/COLOR]" if "dublado" in url2 else "[COLOR blue][L][/COLOR]"
			plus = "+" if "i=" in url2 else ""
			AddDir2(dubleg+"["+season+"]"+plus+" "+metasea["TVShowTitle"].encode('utf-8'), url2, 502, iconimage, iconimage, info="", isFolder=True, background=season, metah=metasea)
			if "dublado" in url2:
				AddDir2("[COLOR blue][L][/COLOR]["+season+"]"+plus+" "+metasea["TVShowTitle"].encode('utf-8'), url2.replace("-dublado",""), 502, iconimage, iconimage, info="", isFolder=True, background=season, metah=metasea)
		except:
			pass
	if Ctrakt != "":
		AddDir("---------- Autoplay ----------" , "", 40, isFolder=False)
		for season,url2 in lista:
			try:
				meta = eval(metah)
				mg = MetadataUtils()
				mmm = mg.get_tvshow_details(title="",tmdb_id=meta['tmdb_id'], ignore_cache=MUcache, lang=MUlang)
				metasea=mergedicts(meta,mmm[int(season)])
				dubleg="[COLOR yellow][D][/COLOR]" if "dublado" in url2 else "[COLOR blue][L][/COLOR]"
				plus = "+" if "i=" in url2 else ""
				AddDir2(dubleg+"["+season+"]"+plus+" "+metasea["TVShowTitle"].encode('utf-8'), url2, 504, "", "", info="", isFolder=False, IsPlayable=True, background=season, metah=metasea)
				if "dublado" in url2:
					AddDir2("[COLOR blue][L][/COLOR]["+season+"]"+plus+" "+metasea["TVShowTitle"].encode('utf-8'), url2, 504, "", "", info="", isFolder=False, IsPlayable=True, background=season, metah=metasea)
			except:
				pass
def animeepisvis(): #502
	try:
		trak = traktS()
		link = common.OpenURL(url)
		lista = re.compile("[^']+\/download").findall(link)
		E = 1
		i = re.compile('i\=(\d+)').findall(url)
		if i:
			E = int(i[0])
		meta = eval(metah)
		for l in lista:
			pc = 1 if meta['imdb_id']+str(meta['season_number'])+str(int(E)) in trak else None
			AddDir2("" ,l, 503, "", "",  isFolder=False, IsPlayable=True, background=str(meta['season_number']), metah=meta, episode=str(E), DL="", playcount=pc)
			E = E + 1
	except:
		pass
def playanimevisauto(): #
	try:
		link = common.OpenURL(url)
		mp4 = re.compile('[^"|\']+\.mp4[^"|\'|\n]*').findall(link)
		qual = re.compile('\/(.{3,4}p)\/').findall( str(mp4) )
		PlayUrl("", mp4[0] + "|referer=http://animesvision.biz/&User-Agent=Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100110 Firefox/11.0", iconimage) 
	except:
		NF("Erro")
		sys.exit()
def playanimevis(): #503
	try:
		link = common.OpenURL(url)
		vid = re.compile('[^"|\']+\.mp4[^"|\'|\n]*').findall(link)
		url2 = re.sub('download$', "", url )
		link2 = common.OpenURL(url2)
		vid2 = re.compile('[^"|\']+\.mp4[^"|\'|\n]*').findall(link2)
		if '/1080p/' in vid[0]:
			vid2.append(re.sub('\/.{3,4}p\/', "/1080p/", vid2[0] ))
		vid3 = vid + vid2
		qual = re.compile('\/(.{3,4}p)\/').findall( str(vid3) )
		d = xbmcgui.Dialog().select("Escolha a qualidade:", qual)
		PlayUrl("", vid3[d] + "|referer=http://animesvision.biz/&User-Agent=Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100110 Firefox/11.0", iconimage) 
	except:
		NF("Erro")
		sys.exit()
# --------------  Trakt
def traktS():
	if not Ctrakt:
		return []
	try:
		headers1 = {'Content-Type': 'application/json','trakt-api-version': '2','trakt-api-key': '888a9d79a643b0f4e9f58b5d4c2b13ee6d8bd584bc72bff8b263f184e9b5ed5d'}
		response_body = common.OpenURL('https://api.trakt.tv/users/'+Ctrakt+'/watched/shows',headers=headers1)
		j=json.loads(response_body)
		trak=[]
	except:
		return []
	for m in j:
		try:
			for Sea in m['seasons']:
				for epi in Sea['episodes']:
					trak.append(m['show']['ids']['imdb']+str(Sea['number'])+str(epi['number']))
		except:
			pass
	return trak	
def traktM():
	#if not Ctrakt:
	#	return []
	headers1 = {'Content-Type': 'application/json','trakt-api-version': '2','trakt-api-key': '888a9d79a643b0f4e9f58b5d4c2b13ee6d8bd584bc72bff8b263f184e9b5ed5d'}
	response_body = common.OpenURL('https://api.trakt.tv/users/'+Ctrakt+'/watched/movies',headers=headers1)
	j=json.loads(response_body)
	trak=[]
	for m in j:
		#ST(j)
		try:
			trak.append(str(m['movie']['ids']['imdb']))
		except:
			pass
	return trak
# --------------  Self
def ultimos_epi():
	#s="Suits,2011,tt1632701;Supernatural,2005,tt0460681;The Big Bang Theory,2007,tt0898266;The Good Doctor,2017,tt6470478;The Flash,2014,tt3107288;The Resident,2018,tt6483832;Arrow,2012,tt2193021;Vikings,2013,tt2306299;Black Lightning,2018,tt6045840;Supergirl,2015,tt4016454;Young Sheldon,2017,tt6226232;Big Little Lies,2017,tt3920596;DC's Legends of Tomorrow,2016,tt4532368;American Crime Story,2016,tt2788432;iZombie,2015,tt3501584;The Walking Dead,2010,tt1520211"
	#s="Suits,2011,tt1632701;The Flash,2014,tt3107288;The Big Bang Theory,2007,tt0898266"
	try:
		link = common.OpenURL("https://pastebin.com/raw/nGhS8V8J")
		series = link.split("\n")
		series.sort()
		#ST(series)
		busca=[]
	except:
		NF("Erro no server")
		return ""
	for m in series:
		try:
			if not "*" in m[0]:
				m2=m.split(",")
				headers1 = {'Content-Type': 'application/json','trakt-api-version': '2','trakt-api-key': '888a9d79a643b0f4e9f58b5d4c2b13ee6d8bd584bc72bff8b263f184e9b5ed5d'}
				response_body = common.OpenURL('https://api.trakt.tv/shows/'+m2[2]+'/last_episode',headers=headers1)
				#busca.append(m2[2])
				j=json.loads(response_body)
				busca.append( [m2[2]+str(j['season'])+str(j['number']), m2[0], j, m2[1], m2[2] ] )
		except:
			pass
	return busca
def moviedb():
	#plugin://plugin.video.elementum/library/show/play/37680/1/1
	#plugin://plugin.video.quasar/library/show/play/37680/1/1
	try:
		v=common.OpenURL("https://api.themoviedb.org/3/find/"+url+"?api_key=bd6af17904b638d482df1a924f1eabb4&language=en-US&external_source=imdb_id")
		#xbmcgui.Dialog().ok('Cube Play', url)
		j = json.loads(v)
		#ST(j["tv_results"][0]["id"])
		#ST(background)
		PlayUrl("", "plugin://plugin.video.elementum/library/show/play/"+str(j["tv_results"][0]["id"])+"/"+background+"/"+episode, "", "")
		#ST("plugin://plugin.video.quasar/library/show/play/"+str(j["tv_results"][0]["id"])+"/"+background+"/"+episode)
	except:
		#ST("erro")
		pass
	#ST(url)
#---------- Downloads
def Baixar(): #302 Baixar
	AddDir("Reload" , "", 40, isFolder=False)
	try:
		#ultimos = common.OpenURL("http://easytvonline.tk/rc/last_episode.php")
		ultimos = ultimos_epi()
	except:
		NF("error")
		return
	trak = traktS()
	arquivos=[]
	DirM = Addon.getSetting("cDir")
	mp4 = []
	for dirname, dirnames, filenames in os.walk(DirM):
		mp4_ = []
		for filename in filenames:
			try:
				url2 = os.path.join(dirname, filename)
				Serie = re.compile("([^\\\|\/]+) \((\d+)\)").findall(dirname)
				Epi = re.compile("s(\d+)e(\d+)",re.IGNORECASE).findall(filename)
				mu = MetadataUtils()
				mmm = mu.get_tvshow_details(title=Serie[0][0],year=Serie[0][1],ignore_cache=MUcache, lang=MUlang)
				if not ".srt" in filename:
					arquivos.append( mmm[-1]['imdb_id']+SEAS(Epi[0][0])+EPI(Epi[0][1]) )
					mp4_.append([Epi[0][0],Epi[0][1], Serie[0][0],filename,url2,mmm[-1]])
				#AddDir("" , dir, 3, "", "", isFolder=False, IsPlayable=True, background=Epi[0][0], metah=(mmm), episode=Epi[0][1], DL="[COLOR pink]"+filename+"[/COLOR] - ")
			except:
				pass
		mp4.append(mp4_)
	for item1 in ultimos:
		try:
			if not item1[0] in arquivos:
				mu = MetadataUtils()
				mmm = mu.get_tvshow_details(title=item1[1],year=item1[3],ignore_cache=MUcache, lang=MUlang)
				exclui=[ item1[1],item1[3], item1[2]['season'], item1[2]['number'] ]
				#AddDir( str(item1[2]['ids']['imdb']), item1[4], 303, "", "", isFolder=False, IsPlayable=True, background=str(item1[2]['season']), metah=mmm , episode=str(item1[2]['number']), DL="[B]"+str(item1[1])+"[/B] ")
				pc = 1 if item1[0] in trak else None
				AddDir2( str(item1[2]['ids']['imdb']), item1[4], 303, "", str(exclui), isFolder=False, IsPlayable=True, background=str(item1[2]['season']), metah=mmm[-1] , episode=str(item1[2]['number']), DL="[B]"+str(item1[1])+"[/B] ", playcount=pc)
				#AddDir( str(item1[2]['ids']['imdb']) , "D:\\mibox\aQuasar\aShows\aSuits (2011)a\Suits (2011) S01E01.strm", 3, "", "", isFolder=False, IsPlayable=True, background=str(item1[2]['season']), metah=mmm , episode=str(item1[2]['number']), DL="[B]"+str(item1[2]['ids']['imdb'])+"[/B] ")
		except:
			NF("erro")
			pass
def Excluir(): #305
	try:
		l = eval(logos)
		folder = os.path.join(DirM, l[0] + " (" + l[1] + ")" )
		season = os.path.join(folder, "Season " +str(l[2]))
		fil = os.path.join(season,  l[0] + ".S"+str(l[2])+"E"+str(l[3])+".strm")
		try:
			os.mkdir(folder)
		except OSError:
			pass
		try:
			os.mkdir(season)
		except OSError:
			pass
		file = open(fil, "w")
		file.close()
		NF("Done")
	except:
		NF("erro")
# --------------  Latest
def AllEpi():
	AddDir("Reload" , "", 40, isFolder=False)
	for dirname, dirnames, filenames in os.walk(DirM):
    # print path to all subdirectories first.
		#for subdirname in dirnames:
			#pass
		for filename in filenames:
			try:
				dir = os.path.join(dirname, filename)
				Serie = re.compile("([^\\\|\/]+) \((\d+)\)").findall(dirname)
				Epi = re.compile("s(\d+)e(\d+)",re.IGNORECASE).findall(filename)
				serie = "The Flash 2014" if "Flash" in Serie[0][0] else Serie[0][0]
				mmm = metahandlers.MetaData().get_meta('tvshow', serie, year=Serie[0][1])
				AddDir("" , dir, 3, "", "", isFolder=False, IsPlayable=True, background=Epi[0][0], metah=(mmm), episode=Epi[0][1], DL="[COLOR pink]"+filename+"[/COLOR] - ")
			except:
				pass

def Latest(): #300
	trak = traktS()
	AddDir("Reload" , "", 40, isFolder=False)
	dl = common.OpenURL("https://pastebin.com/raw/nGhS8V8J")
	dl = re.sub('\*.+', "", dl )
	ml = re.compile("tt\d+").findall(dl)
	DirM = Addon.getSetting("cDir")
	mp4 = []
	file = []
	files = []
	dirs1, files1 = xbmcvfs.listdir(DirM)
	mu = MetadataUtils()
	for d1 in dirs1:
		DirM2 = os.path.join(DirM, d1)
		dirs2, files2 = xbmcvfs.listdir(DirM2)
		imdb = ""
		ano = re.compile(" \(?(\d{2,4})\)?",re.IGNORECASE).findall(d1)
		ano2 = ""
		if ano:
			ano2=ano[0]
		try:	
			mmm = mu.get_tvshow_details(title= re.sub(' \(?\d{2,4}\)?', "", d1 ) , year=ano2, ignore_cache=MUcache, lang=MUlang)
		except:
			ST(d1)
		if "imdb_id" in mmm[-1]:
			imdb = mmm[-1]['imdb_id']
			#ST(str(mmm[-1]),o="a+")
		#ST(d1,o="a+")
		for d2 in dirs2:
			file = []
			DirM3 = os.path.join(DirM2, d2)
			dirs3, files3 = xbmcvfs.listdir(DirM3)
			for f in files3:
				if ".mp4" in f or ".mkv" in f:
					ff = re.compile("s(\d+)e(\d+)",re.IGNORECASE).findall(f)
					if ff:
						s = "S"+ff[0][0]+"E"+ff[0][1]
						im = imdb+str(int(ff[0][0]))+str(int(ff[0][1]))
						file.append([d1, d2, f, s, ff[0][0], ff[0][1], im ] )
			if file:
				file = sorted(file, key=lambda file: file[3], reverse=False)
				files.append([file, mmm[-1]])
	for x, mm in files:
		w = 1
		l=0
		for z in x:
			url2 = os.path.join(DirM, z[0])
			url2 = os.path.join(url2, z[1])
			url2 = os.path.join(url2, z[2])
			try:
				if mm['imdb_id'] in ml:
					if not z[6] in trak and w==1:
						AddDir2( z[2]+" "+z[6],url2, 3, "", "", isFolder=False, IsPlayable=True, metah=mm, background=z[4], episode=z[5], DL="[COLOR maroon]"+re.sub(' \(?\d{2,4}\)?', "", z[0] )+"[/COLOR] ", playcount=0)
						w=0
					else:
						l+=1
					if l == len(x):
						AddDir2( z[2]+" "+z[6],url2, 3, "", "", isFolder=False, IsPlayable=True, metah=mm, background=z[4], episode=z[5], DL="[COLOR lightgreen]"+re.sub(' \(?\d{2,4}\)?', "", z[0] )+"[/COLOR] ", playcount=1)
			except:
				pass
	'''for tvshow, pasta2, file2, ss, S, E, imdb in files:
		tvshow2 = re.sub(' \(?\d{2,4}\)?', "", tvshow )
		#mu = MetadataUtils()
		mmm = mu.get_tvshow_details(title=tvshow2,ignore_cache=MUcache, lang=MUlang)
		if mmm[-1]['imdb_id'] in ml:
			redgreen = "lightgreen" if s[5] == "1" else "maroon"
			pc = 1 if mmm[-1]['imdb_id']+str(int(S))+str(int(E)) in trak else None
			redgreen = "lightgreen" if pc == 1 else "maroon"
			url2 = os.path.join(DirM, tvshow)
			url2 = os.path.join(url2, pasta2)
			url2 = os.path.join(url2, file2)
			AddDir2("",url2, 3, "", "", isFolder=False, IsPlayable=True, background=S, metah=mmm[-1], episode=E, DL="[COLOR "+redgreen+"]"+tvshow2+"[/COLOR] ", playcount=pc)'''
def Next_epi(): #308
	try:
		link = common.OpenURL("https://pastebin.com/raw/nGhS8V8J")
		series = link.split("\n")
		series.sort()
		busca=[]
		for m in series:
			m2=m.split(",")
			headers1 = {'Content-Type': 'application/json','trakt-api-version': '2','trakt-api-key': '888a9d79a643b0f4e9f58b5d4c2b13ee6d8bd584bc72bff8b263f184e9b5ed5d'}
			try:
				response_body = common.OpenURL('https://api.trakt.tv/shows/'+m2[2]+'/next_episode',headers=headers1)
				j=json.loads(response_body)
				#mg = metahandlers.MetaData()
				#meta = mg.get_meta('tvshow', m2[0], imdb_id=m2[2])
				mu = MetadataUtils()
				mmm = mu.get_tvshow_details(title=m2[0],ignore_cache=MUcache, lang=MUlang)
				AddDir2("","", 405, iconimage, iconimage, isFolder=False, IsPlayable=True, background=str(j['season']), metah=mmm[-1], episode=str(j['number']), DL="[COLOR lightgreen]"+m2[0]+"[/COLOR] ")
			except:
				pass
	except:
		pass
# --------------  Fim menu
def mergedicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z
def Series(x): #60
	AddDir("Reload" , "", 40, isFolder=False)
	#mmm = MetadataUtils().get_tvshow_details(title="",tmdb_id="88512", ignore_cache=False, lang=MUlang)
	#ST(mmm)
	#AddDir2( "", "", 69, "", "", isFolder=True, metah=mmm[-1])
	#return
	#l = ["tt0460681","tt6470478","tt3107288","tt6483832","tt2193021","tt6045840","tt4016454","tt6226232","tt4532368","tt2788432","tt3501584","tt6474378"]
	#m = MetadataUtils()
	#mm = m.get_tvshow_details(title="Rick And Morty",ignore_cache=MUcache, lang=MUlang)
	#ST(mm)
	#return
	if "nfewBmAL" in x:
		AddDir("Superflix" , "", 409, isFolder=True)
	if "http" in x:
		try:
			link = common.OpenURL(x)
			link = re.sub('(http.+)\s(http.+)\s(http.+)', r"\1;\2;\3", link )
			link = re.sub('(http.+)\s(http.+)', r"\1;\2", link )
			lista = re.compile("(.+);(.*)\s(.+)").findall(link)
			lista = sorted(lista, key=lambda lista: lista[0])
			#ST(link)
			for name2,id2,url2 in lista:
				try:
					mg = MetadataUtils()
					mmm = mg.get_tvshow_details(title=name2.replace("*",""),tmdb_id=id2, ignore_cache=MUcache, lang=MUlang)
					url3 = url2.split(";")
					serv = ""
					for x in url3:
						if "netcine" in x:
							serv+=" [COLOR yellow][NC][/COLOR]"
						elif "redecanais" in x:
							serv+=" [COLOR blue][RC][/COLOR]"
						elif "mmfilmes" in x:
							serv+=" [COLOR cyan][MM][/COLOR]"
						elif "superflix" in x:
							serv+=" [COLOR lightgreen][SF][/COLOR]"
					if not "asdadsffdsfd" in url2:
						AddDir2(name2 + serv, url2, 69, "", "", isFolder=True, metah=mmm[-1])
				except:
					pass
		except urllib2.URLError, e:
			AddDir("Não foi possível carregar" , "", 0, isFolder=False)
	else:
		AddDir("Nenhuma fonte" , "", 0, isFolder=False)
def Series2(): #69
	url3 = url.split(";")
	name2=[]
	for x in url3:
		if "netcine" in x:
			name2.append("[COLOR yellow][NC][/COLOR]")
		elif "redecanais" in x:
			name2.append("[COLOR blue][RC][/COLOR]")
		elif "mmfilmes" in x:
			name2.append("[COLOR cyan][MM][/COLOR]")
		elif "superflix" in x:
			name2.append("[COLOR lightgreen][SF][/COLOR]")
	if len(url3) > 1:
		d = xbmcgui.Dialog().select("Escolha o servidor:", name2)
	else:
		d=0
	global url
	url = url3[d]
	if "NC" in name2[d]:
		ListSNC(background)
	elif "RC" in name2[d]:
		TemporadasRC(index)
	elif "MM" in name2[d]:
		ListSMM(background)
		setViewS()
	elif "SF" in name2[d]:
		ListSSF()
		setViewS()
# --------------  NETCINE
def ListSNC(x): #61
	trak = traktS()
	#AddDir("Reload" , "", 40, isFolder=False)
	try:
		url2 = re.sub('netcine\.[^\/]+', 'netcine.biz', url)
		link = common.OpenURL(proxy+url2).replace('\n','').replace('\r','').replace('<div class="soci">',"class='has-sub'").replace('\t',"")
		m = re.compile(".emporada (\d+)(.+?class\=\'has-sub\')").findall(link)
		i=1
		if "None" in background: #season
			for season2,epis in m:
				metah2 = eval(metah)
				mu = MetadataUtils()
				mmm = mu.get_tvshow_details(metah2['tmdb_id'],ignore_cache=MUcache, lang=MUlang)
				try:
					metasea=mergedicts(mmm[-1],mmm[int(season2)])
					AddDir2("Temporada "+season2+ " [COLOR yellow][NC][/COLOR]" ,url, 61, iconimage, iconimage, isFolder=True, background=i, metah=metasea)
				except:
					AddDir2("Temporada "+season2+ " [COLOR yellow][NC][/COLOR]" ,url, 61, iconimage, iconimage, isFolder=True, background=i, metah=mmm[-1])
				i+=1
			setViewS()
		else:
			m2 = re.compile("href\=\"([^\"]+).+?(\d+) - (\d+)").findall( m[int(x)-1][1] )
			m3 = re.compile("icon-chevron-right\W+\w\W+([^\<]+)").findall( m[int(x)-1][1] )
			for url2,S,E in m2:
				meta=eval(metah)
				pc = 1 if meta['imdb_id']+background+str(int(E)) in trak else None
				AddDir2("",url2, 62, iconimage, iconimage, isFolder=False, IsPlayable=True, background=background, metah=meta, episode=E, playcount=pc)
				i+=1
			setViewS2()
	except urllib2.URLError, e:
		AddDir("Server NETCINE offline, tente novamente em alguns minutos" , "", 0, isFolder=False)
def PlayS(): #62
	try:
		link = common.OpenURL(proxy+url).replace('\n','').replace('\r','')
		m = re.compile("\"play-.\".+?src=\"([^\"]+)").findall(link)
		listan = re.compile("\#play-...(\w*)").findall(link)
		i=0
		listaf=[]
		listal=[]
		d=""
		if not m:
			xbmcgui.Dialog().ok('Cube Play', 'Vídeo offline')
			sys.exit()
		for url2 in m:
			link3 = common.OpenURL(url2)
			m3 = re.compile("src\=\"(.+campanha[^\"]+)").findall(link3)
			if m3:
				red = common.OpenURL(m3[0])
				red2 = re.compile('redirecionar\.php\?data=([^"]+)').findall(red)
				link4 = common.OpenURL(red2[0])
				link4 = re.sub('window.location.href.+', '', link4)
				link4 = link4.replace("'",'"')
				m4= re.compile("http.+?mp4[^\"]+").findall(link4) 
				m4 = list(reversed(m4))
				for url4 in m4:
					listal.append(url4.replace("';",""))
					dubleg="[COLOR green]HD[/COLOR][/B]" if "ALTO" in url4 else "[COLOR red]SD[/COLOR][/B]"
					listaf.append("[B][COLOR blue]"+listan[i] +"[/COLOR] "+dubleg)
					if "ALTO" in url4:
						d=url4.replace("';","")
			else:
				red = common.OpenURL(url2)
				m3 = re.compile("src\=\"([^\"]+)").findall(red)
				red1 = common.OpenURL(m3[0])
				red2 = re.compile('redirecionar\.php\?data=([^"]+)').findall(red1)
				link4 = common.OpenURL(red2[0],headers={'Cookie': "autorizado=teste; "})
				m5 = re.compile("location.href=\'([^\']+p\=[^\']+)").findall(link4)
				link5 = common.OpenURL(m5[0])
				link5 = re.sub('window.location.href.+', '', link5)
				link5 = link5.replace("'",'"')
				m4= re.compile("http.+?mp4[^\"]+").findall(link5)
				m4 = list(reversed(m4))
				for url4 in m4:
					listal.append(url4.replace("';",""))
					dubleg="[COLOR green]HD[/COLOR][/B]" if "ALTO" in url4 else "[COLOR red]SD[/COLOR][/B]"
					listaf.append("[B][COLOR blue]"+listan[i] +"[/COLOR] "+dubleg)
					if "ALTO" in url4:
						d=url4.replace("';","")
			i+=1
		if d and len(listaf) <= 2:
			d = re.sub('https', 'http', d)
			PlayUrl(name, d+"|Referer=http://cdn.netcine.info&Connection=Keep-Alive&Accept-Language=en&User-Agent=Mozilla%2F5.0+%28compatible%3B+MSIE+10.6%3B+Windows+NT+6.1%3B+Trident%2F6.0%29", iconimage, info)
		else:
			d = xbmcgui.Dialog().select("Escolha a resolução:", listaf)
			if d!= -1:
				listal[d] = re.sub('https', 'http', listal[d])
				PlayUrl(name, listal[d]+"|Referer=http://cdn.netcine.info&Connection=Keep-Alive&Accept-Language=en&User-Agent=Mozilla%2F5.0+%28compatible%3B+MSIE+10.6%3B+Windows+NT+6.1%3B+Trident%2F6.0%29", iconimage, info)
	except urllib2.URLError, e:
		xbmcgui.Dialog().ok('Cube Play', 'Erro, tente novamente em alguns minutos')
		sys.exit()
# --------------  FIM NETCINE
# --------------  redecanais SERIES,ANIMES,DESENHOS
def PlayNextRC(): #138 Next
	#global url
	try:
		url2 = re.sub('redecanais\.[^\/]+', "redecanais.cloud", url.replace("http","http") )
		url2 = re.sub('www.', "", url2 )
		link = common.OpenURL(proxy+url2).replace('\n','').replace('\r','').replace('</html>','<span style="font').replace("http","http")
	except:
		return
	#url = "https://redecanais.cloud/sobrenatural-15a-temporada-episodio-20-continue_be9a5b541.html"
	trak = traktS()
	link = re.sub('<span style="font-size: x-large;">+.+?windows', "", link )
	temps2 = re.compile('size: x-large;\">.+?<span style\=\"font').findall(link)
	inicio = re.compile('i\=(\d+)').findall(url2)
	i = 0
	if inicio:
		for s in range(0, int(inicio[0])):
			del temps2[0]
			i= int(inicio[0])
	epi = re.compile('<strong>(E.+?)<\/strong>(.+?)(<br|<\/p)').findall( temps2[int( background ) -1 ])
	E = "0"
	ee = 0
	for name2,url2,brp in epi:
		ee = ee + 1
		E = str(int(E) + 1)
		urlm = re.compile('href\=\"(.+?)\"(.+?(Dub|Leg))?').findall(url2)
		url2 = re.sub('(\w)-(\w)', r'\1 \2', url2)
		try:
			meta=eval(metah)
			pc = 1 if meta['imdb_id']+background+str(int(E)) in trak else None
			if pc == None:
				global url, episode, background, playcount
				playcount = pc
				episode = E
				url = "http://redecanais.cloud/" + urlm[0][0] if "http" not in urlm[0][0] else urlm[0][0]
				PlaySRC(" - Epi. "+str(ee)+"/"+str(len(epi)))
				return
				sys.exit()
		except:
			pass
	NF("Temporada Completa")
	sys.exit()
def PlaySRC(qq=""): #133 Play series
	try:
		url2 = re.sub('redecanais\.[^\/]+', "redecanais.cloud", url.replace("http","https") )
		link = common.OpenURL(proxy+url2)
		#desc = re.compile('<p itemprop=\"description\"><p>(.+)<\/p><\/p>').findall(link)
		#if desc:
			#desc = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), desc[0]).encode('utf-8')
		player = re.compile('<iframe.{1,50}src=\"(\/?p[^\"]+)\"').findall(link)
		#player = re.sub('^/', "https://www."+RC, player[0])
		if player:
			player = re.sub('^/', "https://"+RC, player[0])
			player = re.sub('.php', 'hlb.php', player)
			player = re.sub('redecanais\.[^\/]+', "gamesgo.fun", player)
			mp4 = common.OpenURL(player ,headers={'referer': RCref})
			try:
				if XBMCPlayer().isPlaying():
					f="1"+1
				player = re.compile('href.{1,5}(mega[^"|\']*)').findall(mp4)
				mp42 = common.OpenURL("https://gamesgo.fun/player3/"+player[0] ,headers={'referer': RCref})
				source = re.compile('source.+').findall(mp42)
				file=re.compile('[^"|\']+\.mp4[^"|\'|\n]*').findall(source[0])
				file[0] = re.sub('https', 'http', file[0])
				tf = testfile(file[0])
				if tf == True:
					NF("2"+qq)
				else:
					f="1"+1
			except:
				NF("1"+qq)
				file=re.compile('src..(http.{1,200}\.mp4[^"|\']*)').findall(mp4)
			file[0] = re.sub('\n', '', file[0])	
			PlayUrl(name, file[0] + "|Referer=https://gamesgo.fun&Connection=Keep-Alive&Accept-Language=en&User-Agent=Mozilla/5.0%20%28Windows%20NT%206.1%3B%20rv%3A11.0%29%20Gecko/20100110%20Firefox/11.0", iconimage, name)
		else:
			NF('Erro RC tente novamente em alguns minutos')
			sys.exit()
	except:
		NF('Erro RC 2 tente novamente em alguns minutos')
		sys.exit()
def TemporadasRC(x): #135 Episodios
	#AddDir("Reload" , "", 40, isFolder=False)
	try:
		url2 = re.sub('redecanais\.[^\/]+', "redecanais.cloud", url.replace("http","http") )
		url2 = re.sub('www.', "", url2 )
		link = common.OpenURL(proxy+url2).replace('\n','').replace('\r','').replace('</html>','<span style="font').replace("http","http")
	except:
		return
	link = re.sub('<span style="font-size: x-large;">+.+?windows', "", link )
	temps = re.compile('(<span style="font-size: x-large;">(.+?)<\/span>)').findall(link)
	inicio = re.compile('i\=(\d+)').findall(url2)
	i = 0
	if inicio:
		for s in range(0, int(inicio[0])):
			del temps[0]
			i= int(inicio[0])
	if x==None:
		for b,tempname in temps:
			tempname = re.compile('\d+').findall(tempname)
			if tempname:
				#if tempname[0]!="0":
				metah2 = eval(metah)
				#ST(metah2)
				mu = MetadataUtils()
				mmm = mu.get_tvshow_details(metah2['tmdb_id'],ignore_cache=MUcache, lang=MUlang)
				try:
					metasea=mergedicts(mmm[-1],mmm[int(tempname[0])])
					AddDir2("Temporada " + tempname[0] + " [COLOR blue][RC][/COLOR]", url, 135, iconimage, iconimage, info="", isFolder=True, index=i, background=tempname[0], metah=metasea)
				except:
					AddDir2("Temporada " + tempname[0] + " [COLOR blue][RC][/COLOR]", url, 135, iconimage, iconimage, info="", isFolder=True, index=i, background=tempname[0], metah=metasea)
				i+=1
	if x==None:
		for b,tempname in temps:
			tempname = re.compile('\d+').findall(tempname)
			if tempname:
				metah2 = eval(metah)
				mu = MetadataUtils()
				mmm = mu.get_tvshow_details(metah2['tmdb_id'],ignore_cache=MUcache, lang=MUlang)
				try:
					metasea=mergedicts(mmm[-1],mmm[int(tempname[0])])
					AddDir2("Play Temp. " + tempname[0] + " [COLOR blue][RC][/COLOR]", url, 138, iconimage, iconimage, info="", isFolder=False, index=i, background=tempname[0], metah=metasea, IsPlayable=True)
				except:
					AddDir2("Play Temp. " + tempname[0] + " [COLOR blue][RC][/COLOR]", url, 138, iconimage, iconimage, info="", isFolder=False, index=i, background=tempname[0], metah=metasea, IsPlayable=True)
				i+=1
		AddDir("Todos Episódios" ,url, 139, iconimage, iconimage, metah=eval(metah))
		setViewS()
	else:
		trak = traktS()
		temps2 = re.compile('size: x-large;\">.+?<span style\=\"font').findall(link)
		#x=int(x)-1
		epi = re.compile('<strong>(E.+?)<\/strong>(.+?)(<br|<\/p)').findall(temps2[int(x)])
		E = "0"
		for name2,url2,brp in epi:
			#E = re.compile('\d+').findall(name2)
			#if E:
			#	E=E[0]
			#else:
			#	E="1"
			E = str(int(E) + 1)
			urlm = re.compile('href\=\"(.+?)\"(.+?(Dub|Leg))?').findall(url2)
			url2 = re.sub('(\w)-(\w)', r'\1 \2', url2)
			#if urlm:
			#	urlm[0] = "http://www.redecanais.xyz/" + urlm[0] if "http" not in urlm[0] else urlm[0]
			#if len(urlm) > 1:
			#	urlm[1] = "http://www.redecanais.xyz/" + urlm[1] if "http" not in urlm[1] else urlm[1]
			#	AddDir("" ,urlm[0], 133, "", "",  isFolder=False, IsPlayable=True, background=background, metah=eval(metah), episode=E, DL="[COLOR yellow](D)[/COLOR] ")
			#	AddDir("" ,urlm[1], 133, "", "",  isFolder=False, IsPlayable=True, background=background, metah=eval(metah), episode=E, DL="[COLOR blue](L)[/COLOR] ")
			#elif urlm:
			#	AddDir("" ,urlm[0], 133, "", "",  isFolder=False, IsPlayable=True, background=background, metah=eval(metah), episode=E, DL="")
			try:
				urlm2 = "http://redecanais.cloud/" + urlm[0][0] if "http" not in urlm[0][0] else urlm[0][0]
				dubleg="[COLOR yellow](D)[/COLOR] "
				if "Dub" in urlm[0][2]:
					dubleg = "[COLOR yellow](D)[/COLOR] "
				elif "Leg" in urlm[0][2]:
					dubleg = "[COLOR blue](L)[/COLOR] "
				meta=eval(metah)
				pc = 1 if meta['imdb_id']+background+str(int(E)) in trak else None
				AddDir2("" ,urlm2, 133, "", "",  isFolder=False, IsPlayable=True, background=background, metah=meta, episode=E, DL=dubleg, playcount=pc)
			except:
				pass
		E = "0"
		for name2,url2,brp in epi:
			E = str(int(E) + 1)
			urlm = re.compile('href\=\"(.+?)\"(.+?(Dub|Leg))?').findall(url2)
			url2 = re.sub('(\w)-(\w)', r'\1 \2', url2)
			try:
				urlm2 = "http://redecanais.cloud/" + urlm[1][0] if "http" not in urlm[1][0] else urlm[1][0]
				dubleg="[COLOR yellow](D)[/COLOR] "
				if "Dub" in urlm[1][2]:
					dubleg = "[COLOR yellow](D)[/COLOR] "
				elif "Leg" in urlm[1][2]:
					dubleg = "[COLOR blue](L)[/COLOR] "
				meta=eval(metah)
				pc = 1 if meta['imdb_id']+background+str(int(E)) in trak else None
				#AddDir("" ,urlm2, 133, "", "",  isFolder=False, IsPlayable=True, background=background, metah=eval(metah), episode=E, DL=dubleg, playcount=pc)
				AddDir2("" ,urlm2, 133, "", "",  isFolder=False, IsPlayable=True, background=background, metah=meta, episode=E, DL=dubleg, playcount=pc)
			except:
				pass
		setViewS2()
def AllEpisodiosRC(): #139 Mostrar todos Epi
	url2 = re.sub('redecanais\.[^\/]+', "redecanais.cloud", url.replace("http","http") )
	link = common.OpenURL(proxy+url)
	match = re.compile('<strong>(E.+?)<\/strong>(.+?)(<br|<\/p)').findall(link)
	S= 0
	if match:
		for name2,url2,brp in match:
			E = re.compile('\d+').findall(name2)
			if E:
				E=E[0]
				if int(E) == 1:
					S = S + 1
			else:
				E="1"
			urlm = re.compile('href\=\"(.+?)\"').findall(url2)
			if urlm:
				if "http" not in urlm[0]:
					urlm[0] = "http://redecanais.cloud/" + urlm[0]
			if len(urlm) > 1:
				if "http" not in urlm[1]:
					urlm[1] = "http://redecanais.cloud/" + urlm[1]
				AddDir("" ,urlm[0], 133, "", "",  isFolder=False, IsPlayable=True, background=str(S), metah=eval(metah), episode=E, DL="[COLOR yellow](D)[/COLOR] ")
				AddDir("" ,urlm[1], 133, "", "",  isFolder=False, IsPlayable=True, background=str(S), metah=eval(metah), episode=E, DL="[COLOR blue](L)[/COLOR] ")
			elif urlm:
				AddDir("" ,urlm[0], 133, "", "",  isFolder=False, IsPlayable=True, background=str(S), metah=eval(metah), episode=E, DL="")

def PlayMRC2(): #96 Play filmes
	url2 = re.sub('redecanais\.[^\/]+', RC, url.replace("http\:","https\:") )
	if not "redecanais" in url2:
		url2 = "https://"+RC+ url2
	try:
		link = common.OpenURL(proxy+url2.replace("http\:","https\:"))
		player = re.compile('<iframe.{1,50}src=\"(\/?p[^\"]+)\"').findall(link)
		if player:
			player = re.sub('^/', "https://"+RC, player[0])
			player = re.sub('\.php', "hlb.php", player)
			player = re.sub('redecanais\.[^\/]+', "gamesgo.fun", player)
			mp4 = common.OpenURL(player ,headers={'referer': RCref})
			try:
				player = re.compile('href.{1,5}(mega[^"|\']*)').findall(mp4)
				mp42 = common.OpenURL("https://gamesgo.fun/player3/"+player[0] ,headers={'referer': RCref})
				source = re.compile('source.+').findall(mp42)
				file=re.compile('[^"|\']+\.mp4[^"|\'|\n]*').findall(source[0])
				file[0] = re.sub('https', 'http', file[0])
				tf = testfile(file[0])
				if tf == True:
					NF(2)
				else:
					f="1"+1
			except:
				NF(1)
				file=re.compile('src..(http.{1,200}\.mp4[^"|\']*)').findall(mp4)
			if len(str(metah))>10:
				mm= eval(metah)
				mm['title']=background
			else:
				mg = metahandlers.MetaData()
				mm = mg.get_meta('movie', "", tmdb_id=iconimage)
			file[0] = re.sub('\n', '', file[0])
			PlayUrl2("", file[0] + "|referer=http://gamesgo.fun&User-Agent=Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100110 Firefox/11.0&redecanaisAS", iconimage, metah=mm) #aqui
		else:
			NF("Server error. Tente novamente em alguns minutos 2")
			sys.exit()
	except:
		NF("Server error. Tente novamente em alguns minutos")
		sys.exit()
		
# ----------------- FIM redecanais SERIES,ANIMES,DESENHOS
def testfile(url):
	try:
		headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100110 Firefox/11.0' }
		req = urllib2.Request(url, None, headers)
		req.headers['Range'] = 'bytes=%s-%s' % (100, 350)
		f = urllib2.urlopen(req).read()
		return True
	except:
		return False
def Elementum(): #97
	l = ["[COLOR blue]RedeCanais[/COLOR]","[COLOR white]Elementum[/COLOR]"]
	if CEle == "1":
		d = 0
	elif CEle == "2":
		d = 1
	else:
		d = xbmcgui.Dialog().select("Selecione o server:", l)
	if d == 0:
		PlayMRC2()
	elif d == 1:
		v=common.OpenURL("https://api.themoviedb.org/3/movie/"+iconimage+"?api_key=bd6af17904b638d482df1a924f1eabb4&language=en-US&external_source=imdb_id")
		j = json.loads(v)
		listitem = xbmcgui.ListItem(path="plugin://plugin.video.elementum/library/movie/play/"+j['imdb_id']+"?doresume=true")
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def PlayUrl2(name, url, iconimage=None, info='', sub='', metah=''):
	RS = ReadSeek(metah['imdb_id'])
	url = re.sub('\.mp4$', '.mp4?play', url)
	url = common.getFinalUrl(url)
	xbmc.log('--- Playing url2 "{0}". {1}'.format(name, url), 2)
	listitem = xbmcgui.ListItem(path=url)
	#listitem = xbmcgui.ListItem(path="D:\S\Shows\Under Pressure (2017)\SOBPRSAOS02E02.mp4")
	if metah:
		listitem.setProperty('StartPercent', RS)
		listitem.setArt({"thumb": metah['cover_url'], "poster": metah['cover_url'], "banner": metah['cover_url'], "fanart": metah['backdrop_url'] })
		listitem.setInfo(type="Video", infoLabels=metah)
	else:
		listitem.setInfo(type="Video", infoLabels={"mediatype": "video", "Title": name, "Plot": info })
	if sub!='':
		listitem.setSubtitles(['special://temp/example.srt', sub ])
	if iconimage is not None:
		try:
			listitem.setArt({'thumb' : iconimage})
		except:
			listitem.setThumbnailImage(iconimage)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
	
	player = XBMCPlayer()
	xbmc.sleep(2000)
	#xbmc.sleep(200)
	monitor = xbmc.Monitor()
	while not monitor.abortRequested():
		if player.isPlaying():
			try:
				if "redecanaisAS" in player.getPlayingFile():
					#NF(player.getVideoInfoTag().getIMDBNumber())
					#ST(player.getVideoInfoTag().getIMDBNumber())
					#xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, str(100*player.getTime()/player.getTotalTime()), "", icon))
					player.totalTime=player.getTotalTime()
					player.gTime=player.getTime()
					player.id=player.getVideoInfoTag().getIMDBNumber()
					#ST(str(player.gTime)+" "+str(player.getTime()))
					#ST(player.getVideoInfoTag().getIMDBNumber())
					AddSeek(player.id,player.gTime,player.totalTime)
			except:
				pass
		else:
			xbmc.sleep(1000)
			#xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, "close", "", icon))
			#AddSeek(player.id,str(100*player.gTime/player.totalTime))
			#Biblioteca()
			break
		if monitor.waitForAbort(120):
			break
		#xbmc.log("hello addon! %s" % time.time(), level=xbmc.LOGNOTICE)
		#xbmc.log('--- Playing', 2)

# ----------------- Inicio MM filmes Series
def ListSMM(x): #191
	link = common.OpenURL(url)
	m = re.compile('boxp\(.([^\']+)').findall(link)
	i=1
	if m:
		if x=="None":
			link2 = common.OpenURL(m[0],headers={'referer': "http://www.mmfilmes.tv/"})
			m2 = re.compile('opb\(.([^\']+).+?.{3}.+?[^\\>]+.([^\<]+)').findall(link2)
			listar=[]
			listal=[]
			for link,res in m2:
				listal.append(link)
				listar.append(res)
			if len(listar)==1:
				d=0
			else:
				d = xbmcgui.Dialog().select("Selecione o server:", listar)
			if d== -1:
				d= 0
			if m2:
				link3 = common.OpenURL(m2[0][0],headers={'referer': "http://www.mmfilmes.tv/"}).replace("\n","").replace("\r","").replace('".Svplayer"',"<end>").replace('\t'," ")
				link3 = re.sub('(\(s \=\= \d+\))', r'<end>\1', link3 )
				m3 = re.compile('s \=\= (\d+)(.+?\<end\>)').findall(link3)
				for temp in m3:
					metah2 = eval(metah)
					mg = metahandlers.MetaData()
					ms = mg.get_seasons(metah2['TVShowTitle'], metah2['tvdb_id'], [i])
					if ms[0]['cover_url']:
						metah2['cover_url'] = ms[0]['cover_url']
					AddDir("Temporada "+ temp[0] +" [COLOR cyan][MM][/COLOR]" ,listal[d], 192, iconimage, iconimage, isFolder=True, background=i, metah=metah2)
					i+=1
def ListEpiMM(x): #192
	trak = traktS()
	link3 = common.OpenURL(url,headers={'referer': "http://www.mmfilmes.tv/"}).replace("\n","").replace("\r","").replace('".Svplayer"',"<end>").replace('\t'," ")
	link3 = re.sub('(\(s \=\= \d+\))', r'<end>\1', link3 )
	m3 = re.compile('s \=\= (\d+)(.+?\<end\>)').findall(link3)
	r=-1
	p=1
	dubleg = re.compile("t \=\= \'([^\']+)(.+?\})").findall( m3[int(x) -1][1] )
	epi = re.compile("e \=\= (\d+).+?addiframe\(\'([^\']+)").findall( m3[int(x) -1][1] )
	for E,url2 in epi:
		url2 = "https://player.mrhd.tv/" + url2 if not "http" in url2 else url2
		if p == int(E) :
			r+=1
		if len(dubleg[r][1]) < 30:
			r+=1
		meta=eval(metah)
		pc = 1 if meta['imdb_id']+background+str(int(E)) in trak else None
		dl = "[COLOR yellow](D)[/COLOR] " if "dub" in dubleg[r][0] else "[COLOR blue](L)[/COLOR] "
		AddDir("",url2, 194, iconimage, iconimage, isFolder=False, IsPlayable=True, background=background, metah=meta, episode=E, DL=dl, playcount=pc)
	setViewS2()
def PlaySMM(): #194
	if "drive.google" in url:
		#xbmcgui.Dialog().ok('Cube Play', 'Erro, video não encontrado, drive')
		PlayUrl(name, "plugin://plugin.video.gdrive?mode=streamURL&url="+url.encode('utf-8'), iconimage, info)
		sys.exit()
	cdn = re.compile('(\d+)\=(.+?.mp4)|\&l\=(.+)').findall(url)
	if cdn:
		cdn = list(reversed(cdn))
		listar=[]
		listal=[]
		legenda=""
		for res,link,leg in cdn:
			if link <> "":
				listal.append(link)
				listar.append(res)
			if leg:
				legenda = leg
				if not "http" in legenda:
					legenda = "http://player.mmfilmes.tv/" + legenda
				legenda = re.sub(' ', '%20', legenda )
		d = xbmcgui.Dialog().select("Selecione a resolução, cdn", listar)
		if d!= -1:
			url2 = re.sub(' ', '%20', listal[d] )
			PlayUrl(name, url2, iconimage, info, sub=legenda)
	else:
		link2 = common.OpenURL( re.sub('(\/.{1,25}\/).{1,10}\/', r'\1', url) ,headers={'referer': "http://player.mmfilmes.tv"}).replace('"',"'")
		m2 = re.compile('(h[^\']+).+?label...(\w+)').findall(link2)
		legenda = re.compile('([^\']+\.(vtt|srt|sub|ssa|txt|ass))').findall(link2)
		listar=[]
		listal=[]
		for link,res in m2:
			listal.append(link)
			listar.append(res)
		if len(listal) < 1:
			xbmcgui.Dialog().ok('Cube Play', 'Erro!')
			sys.exit(int(sys.argv[1]))
		d = xbmcgui.Dialog().select("Selecione a resolução", listar)
		if d!= -1:
			url2 = re.sub(' ', '%20', listal[d] )
			if legenda:
				legenda = re.sub(' ', '%20', legenda[0][0] )
				if not "http" in legenda:
					legenda = "https://player.mrhd.tv/" + legenda
				PlayUrl(name, url2, iconimage, info, sub=legenda)
			else:
				PlayUrl(name, url2, iconimage, info)
# --------------  FIM MMfilmes
# ----------------- Inicio Superflix
def ListSSF(): #401
	l = common.OpenURL(url).replace("\n","").replace("\r","")
	m = re.compile('Temporada ?.{5,6}(\d+)(.+?)\<\/Season\>').findall(l)
	for temp2,cont2 in m:
		metah2 = eval(metah)
		#ST(metah2)
		mu = MetadataUtils()
		mmm = mu.get_tvshow_details(metah2['tmdb_id'],ignore_cache=MUcache, lang=MUlang)
		try:
			metasea=mergedicts(mmm[-1],mmm[int(temp2)])
			AddDir2("Temporada "+ temp2 +" [COLOR lightgreen][SF][/COLOR]" ,cont2, 402, iconimage, iconimage, isFolder=True, background=int(temp2), metah=metasea)
		except:
			#NF(temp2)
			AddDir2("Temporada "+ temp2 +" [COLOR lightgreen][SF][/COLOR]" ,cont2, 402, iconimage, iconimage, isFolder=True, background=int(temp2), metah=mmm[-1])
def ListEpiSF(): #402
	trak = traktS()
	epis = re.compile('Num.{1,2}(\d+).+?(http:[^\"]+)').findall(url)
	#ST(url)
	for E,url2 in epis:
		meta=eval(metah)
		pc = 1 if meta['imdb_id']+background+str(int(E)) in trak else None
		AddDir2("",url2, 405, iconimage, iconimage, isFolder=False, IsPlayable=True, background=background, metah=meta, episode=str(E), DL="", playcount=pc)
def PlaySSF(): #405
	#PlayUrl(name, "plugin://plugin.video.gdrive?mode=streamURL&amp;url=https://lh4.googleusercontent.com/zHFt1HqE5lblW_XBVAULwcU84_Z1Dyb9vvsPuqNcfvjPeuFYy_89w9tsp9U=s61","","")
	try:
		l = common.OpenURL(url)
		#l = common.OpenURL("http://www.superflix.net/episodio/the-walking-dead-10x2/")
		m = re.compile("term\-(\d{3,10})").findall(l) # numero
		legsub = re.compile("data-tplayernv.+?<span>([^\<]+)").findall(l.replace("<span>SuperFlix</span>",""))
		if not legsub:
			xbmcgui.Dialog().ok('Cube Play', "Episódio ainda não disponível")
			sys.exit()
		if len(legsub) == 1:
			d = 0
			NF(legsub[0])
		else:
			d = xbmcgui.Dialog().select("Escolha:", legsub)
		if not d == -1:
			trem = "http://www.superflix.net/?trembed="+str(d)+"&trid="+m[0]+"&trtype=2" # www.superflix.net/?trembed=1&trid=58826&trtype=2
			l2 = common.OpenURL(trem)
			m2 = re.compile("(http.+?(\w{28,35}))").findall(l2)
			msub = re.compile("vlsub\=([^\"|?]+)").findall(l2)
			if not m2:
				PlaySSF2(l2)
				sys.exit()
		try:
			leg = "https://sub.sfplayer.net/subdata/"+msub[0] if msub else ""
			leg2 = msub[0]
		except:
			leg = ""
		mp4 = RetLinkSF(m2[0][0],m2[0][1])
		if not mp4:
			sys.exit()
		mp4m = re.compile("RESOLUTION\=.+x([^\s]+)\n(.+)").findall(mp4[1])
		if not mp4m:
			mp42 = mp4[0]+"/hls/"+m2[0][1]+".playlist.m3u8"
			PlayUrl(name, mp42, iconimage, info, sub=leg)
			sys.exit()
		mp4m = sorted(mp4m, key=lambda k: k[0], reverse=True)
		mp4r=[]
		mp4u=[]
		for res2,url2 in mp4m:
			mp4r.append(res2.replace("999","1080")+"p")
			mp4u.append(url2)
		d2 = xbmcgui.Dialog().select("Escolha a resolução:", mp4r)
		if not d2 == -1:
			NF("plus")
			ST("http://pat-197972:8080/sf/merge2.php?l="+mp4[0]+mp4u[d2]+"&sub="+leg)
			v = baixarsf(mp4[0]+mp4u[d2])
			if v:
				PlayUrl(name, v, iconimage, info, sub=leg)
			else:
				NF("nao")
			#PlayUrl(name, "http://pat-197972:8080/sf/list.php?u="+mp4[0]+mp4u[d2], iconimage, info, sub=leg)
		system.exit()
		#PlayUrl(name, "plugin://plugin.video.gdrive?mode=streamURL&amp;url="+"https://slave2.sfplayer.net/hls/a6ebb20cd567cc52309a965ee2cd82b7.playlist.m3u8", iconimage, info, sub=leg)
	except:
		sys.exit()
def RetLinkSF(link,x):
	#plus = "plus" if "plus" in link else ""
	plus = "hls"
	for s in range(1, 8):
		x2 = "https://slave"+str(s)+plus+".sfplayer.net/hls2/"+x+".playlist.m3u8"
		try:
			NF(s,t=500)
			l = common.OpenURL(x2, headers={'referer': "https://www.superflix.net/"})
			if len(l) > 20:
				return ["https://slave"+str(s)+plus+".sfplayer.net",l.replace("1080","999")]
		except urllib2.URLError, e:
			NF("offline")
			return ""
def PlaySSF2(x):
	api = re.compile("http[^\"]+api[^\"]+").findall(x)
	if not api:
		sys.exit()
	l = common.OpenURL(api[0])
	m = re.compile("iframe.{1,10}(http[^\"]+api[^\"]+)").findall(l)
	l2 = common.OpenURL(m[0])
	m2 = re.compile('http[^\"]+file.{1,5}\/([^\/"]+)').findall(l2)
	url2 = "https://drive.google.com/file/d/"+m2[0]+"/edit"
	PlayUrl(name, "plugin://plugin.video.gdrive?mode=streamURL&amp;url="+url2.encode('utf-8'), iconimage, info)
def LatestSSF(): #409
	AddDir("Reload" , "", 40, isFolder=False)
	try:
		l = common.OpenURL("http://easytvonline.tk/rc/leg/pb2.php")
		m = re.compile("(.+;.+)\s").findall(l)
		for x in m:
			s = x.split(";")
			mu = MetadataUtils()
			mmm = mu.get_tvshow_details(title=s[1],ignore_cache=MUcache, lang=MUlang)
			redgreen = "lightgreen" if s[5] == "1" else "maroon"
			AddDir2("","", 405, iconimage, iconimage, isFolder=False, IsPlayable=True, background=s[2], metah=mmm[-1], episode=s[3], DL="[COLOR "+redgreen+"]"+s[1]+"[/COLOR] ", playcount=s[5])
	except:
		sys.exit()
def baixarsf(link=""):
	Path = xbmc.translatePath( xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
	py = os.path.join( Path, "vid.mp4")
	file = open(py, "w")
	file.write("\n")
	if link == "":
		return
	m3u = common.OpenURL(link, headers={'referer': "https://www.superflix.net/"})
	m = re.compile("http.+").findall(m3u)
	q = 0
	progress = xbmcgui.DialogProgress()
	progress.create('Downloading...')
	b = 0
	for s in m:
		if (progress.iscanceled()):
			baixarsf()
			return
		q+=1
		try:
		#if q == 15:	break
			per = int(q*100/len(m))
			filedata = urllib2.urlopen(s).read()
			b += len(filedata)
			progress.update(per, convert_size( b ), "", str(per) +'%')
			file = open(py, "ab+")
			file.write(filedata)
		except:
			progress.close()
			NF("erro")
			return
	progress.close()
	return py
# ----------------- FIM Superflix
def PlayUrl(name, url, iconimage=None, info='', sub=''):
	#if DirM in url:
		#sub=re.sub('\..{3}$', '.srt', url)
	#url = re.sub('\.mp4$', '.mp4?play', url)
	url = common.getFinalUrl(url)
	xbmc.log('--- Playing "{0}". {1}'.format(name, url), 2)
	listitem = xbmcgui.ListItem(path=url)
	if metah:
		try:
			metah2 = eval(metah)
			mg = MetadataUtils()
			eInfo_ = mg.get_episode_details(metah2['tmdb_id'], SEAS(background), EPI(episode))
			eInfo = mergedicts(metah2,eInfo_)
			eInfo["Title"]= eInfo["TVShowTitle"]
			S=str(eInfo['season'])
			E=str(eInfo['episode'])
			listitem.setArt({"poster": eInfo['cover_url'], "banner": eInfo['cover_url'], "fanart": eInfo['backdrop_url'] })
			eInfo.pop('cast', 1)
			listitem.setInfo( type="Video", infoLabels= eInfo )
			listitem.setInfo( type="Video", infoLabels= {'genre': '[COLOR blue]S'+str(eInfo['season'])+'E'+str(eInfo['episode'])+'[/COLOR]: '+eInfo['EpisodeTitle']} )
		except:
			try:
				metah2 = eval(metah)
				metah2['Title'] = metah2['TVShowTitle']
				metah2['season'] = int(background)
				metah2['episode'] = int(episode)
				metah2['genre'] = '[COLOR blue]S'+str( SEAS(background) )+'E'+str( EPI(episode) )+'[/COLOR]'
				listitem.setInfo( type="Video", infoLabels= metah2 )
			except:
				pass
	else:
		listitem.setInfo(type="Video", infoLabels={"mediatype": "video", "Title": name, "Plot": info })
		if iconimage is not None:
			try:
				listitem.setArt({'thumb' : iconimage})
			except:
				listitem.setThumbnailImage(iconimage)
	#if sub!='':
		#listitem.setSubtitles(['special://temp/example.srt', sub ])
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
	'''player = XBMCPlayer()
	xbmc.sleep(500)
	monitor = xbmc.Monitor()
	while not monitor.abortRequested():
		#ST(100*player.getTime()/player.getTotalTime())
		if monitor.waitForAbort(20):
			break
		#xbmc.log("hello addon! %s" % time.time(), level=xbmc.LOGNOTICE)
		if not player.isPlaying():
			xbmc.sleep(500)
			break'''
def Data(x):
	x = eInfo = re.sub('\d\d(\d+)\-(\d+)\-(\d+)', r'\3/\2/\1', x )
	return "[COLOR yellow]("+x+")[/COLOR]"
def EPI(x):
	x = re.sub('[0]+(\d+)', r'\1', x )
	return str(x)
def SEAS(x):
	x = re.sub('0(\d)', r'\1', x )
	return str(x)
def AddDir(name, url, mode, iconimage='', logos='', index="", move=0, isFolder=True, IsPlayable=False, background=None, cacheMin='0', info='', DL='', year='', metah={}, episode='', playcount=None):
	urlParams = {'name': name, 'url': url, 'mode': mode, 'iconimage': iconimage, 'logos': logos, 'cache': cacheMin, 'index': index, 'info': info, 'background': background, 'DL': DL, 'year': year, 'metah': metah, 'episode': episode, 'playcount': playcount}
	if metah:
		if background and episode:
			mg = metahandlers.MetaData()
			#sInfo = mg.get_seasons(metah['TVShowTitle'], metah['imdb_id'], [1])
			eInfo = mg.get_episode_meta(metah['TVShowTitle'], metah['imdb_id'], SEAS(background), EPI(episode))
			#liz=xbmcgui.ListItem(DL+background+"."+EPI(episode)+" "+eInfo['title'] +" "+Data(eInfo['premiered'])+ " [COLOR blue]["+str(eInfo['rating'])+"][/COLOR]", iconImage=metah['cover_url'], thumbnailImage=metah['cover_url'])
			liz=xbmcgui.ListItem(DL+background+"x"+EPI(episode)+". "+eInfo['title'], iconImage=metah['cover_url'], thumbnailImage=metah['cover_url'])
			#liz.setRating("imdb", 0.1, 8940, False)
			liz.setArt({"thumb": eInfo['cover_url'], "poster": eInfo['cover_url'], "banner": eInfo['cover_url'], "fanart": eInfo['backdrop_url'] })
			infoLabels = metah
			eInfo['userrating'] = eInfo['rating']
			eInfo['mediatype'] = u'tvshow'
			if playcount:
				eInfo['playcount'] = playcount
			else:
				eInfo.pop('playcount', 1)
			liz.setInfo( type="Video", infoLabels= eInfo )
			#liz.setInfo( type='Video', {'premiered': '2018-01-01'} )
			#liz.setInfo('video', { 'Premiered': '01-01-2018' })
			#ST(SEAS(background))
			#eInfo = re.sub('\'duration\'\:[^,]+,', '', str(eInfo) )
			#eInfo = eval(eInfo)
			#liz.setRating("imdb", 4.6, 8940, False)
			#a = mg.get_seasons("Supergirl", "tt4016454", [1])
			#ST(a)
		else:
			metah['mediatype'] = u'tvshow'
			metah['Imdbnumber'] = metah['imdb_id']
			if playcount:
				metah['playcount'] = playcount
			else:
				metah.pop('playcount', 1)
			#metah['cast']=['a','b']
			liz=xbmcgui.ListItem(DL +" "+name, iconImage=metah['cover_url'], thumbnailImage=metah['cover_url'])
			liz.setArt({"poster": metah['cover_url'], "banner": metah['cover_url'], "fanart": metah['backdrop_url'] })
			liz.setInfo( type="Video", infoLabels= metah )
	else:
		liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage )
		liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": info, "Imdbnumber": "tt0460681" })
		liz.setArt({"poster": iconimage, "banner": logos, "fanart": logos })
		#listMode = 21 # Lists
	if IsPlayable:
		liz.setProperty('IsPlayable', 'true')
	items = []
	if mode == 1 or mode == 2:
		items = []
	elif mode == 96 and logos <> "":
		liz.addContextMenuItems(items = [("Elementum", 'XBMC.RunPlugin(plugin://plugin.video.elementum/library/movie/play/{0}?play&doresume=true)'.format(logos)) ])
	elif mode == 303:
		liz.addContextMenuItems(items = [("Excluir da lista", 'XBMC.RunPlugin({0}?mode=305&logos={1})'.format(sys.argv[0], urllib.quote_plus(logos) ))])
	elif mode == 96:
		liz.addContextMenuItems(items = [("Excluir da lista", 'XBMC.RunPlugin({0}?url={1}&mode=355&iconimage={2}&name={3}&index={4})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name), index))])
	if mode == 10:
		urlParams['index'] = index
	u = '{0}?{1}'.format(sys.argv[0], urllib.urlencode(urlParams))
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)
	
def AddDir2(name, url, mode, iconimage='', logos='', index="", move=0, isFolder=True, IsPlayable=False, background=None, cacheMin='0', info='', DL='', year='', metah={}, episode='', playcount=None): #add2
	urlParams = {'name': name, 'url': url, 'mode': mode, 'iconimage': iconimage, 'logos': logos, 'cache': cacheMin, 'index': index, 'info': info, 'background': background, 'DL': DL, 'year': year, 'metah': metah, 'episode': episode, 'playcount': playcount}
	if metah:
		if background and episode:
			mg = MetadataUtils()
			eInfo = mg.get_episode_details(metah['tmdb_id'], SEAS(background), EPI(episode), ignore_cache=MUcacheEpi, lang=MUlang)
			eInfo2 = mergedicts(metah,eInfo)
			eInfo2['playcount'] = 1 if playcount else 0
			#eInfo2['userrating'] = eInfo2['rating']
			if 'EpisodeTitle' in eInfo2:
				liz=xbmcgui.ListItem(DL+"[COLOR white]"+background+"x"+EPI(episode)+". "+eInfo2['EpisodeTitle']+"[/COLOR]", iconImage=metah['cover_url'], thumbnailImage=metah['cover_url'])
			else:
				liz=xbmcgui.ListItem(DL+"[COLOR white]"+background+"x"+EPI(episode)+". Episode "+EPI(episode)+"[/COLOR]", iconImage=metah['cover_url'], thumbnailImage=metah['cover_url'])
			if ".jpg" in eInfo2['imagepi']:
				liz.setArt({"thumb": eInfo2['imagepi'], "poster": eInfo2['cover_url'], "banner": eInfo2['cover_url'], "fanart": eInfo2['backdrop_url'] })
			else:
				liz.setArt({"thumb": eInfo2['cover_url'], "poster": eInfo2['cover_url'], "banner": eInfo2['cover_url'], "fanart": eInfo2['backdrop_url'] })
			if "cast" in eInfo2:
				liz.setCast(eInfo2['cast'])
			#ST(eInfo2)
			eInfo2.pop('cast', 1)
			liz.setInfo( type="Video", infoLabels= eInfo2 )
		else:
			liz=xbmcgui.ListItem(DL +""+name, iconImage=metah['cover_url'], thumbnailImage=metah['cover_url'])
			liz.setArt({"poster": metah['cover_url'], "banner": metah['cover_url'], "fanart": metah['backdrop_url'] })
			if "cast" in metah:
				liz.setCast(metah['cast'])
			metah.pop('cast', 1)
			metah['tagline'] = re.sub('\[(.+)\]', r'\1', str(metah['genre']) )
			metah['tagline'] = re.sub("u\'(.+?)\'", r'\1', metah['tagline'] ) 
			#ST( )
			metah['plot'] = metah['plot2'] if metah['plot2'] else metah['plot']
			liz.setInfo( type="Video", infoLabels= metah )
	else:
		liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage )
		liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": info })
		liz.setArt({"poster": iconimage, "banner": logos, "fanart": logos })
		#listMode = 21 # Lists
	if IsPlayable:
		liz.setProperty('IsPlayable', 'true')
	items = []
	if mode == 1 or mode == 2:
		items = []
	elif mode == 96 and logos <> "":
		liz.addContextMenuItems(items = [("Elementum", 'XBMC.RunPlugin(plugin://plugin.video.elementum/library/movie/play/{0}?play&doresume=true)'.format(logos)) ])
	elif mode == 303:
		liz.addContextMenuItems(items = [("Excluir da lista", 'XBMC.RunPlugin({0}?mode=305&logos={1})'.format(sys.argv[0], urllib.quote_plus(logos) ))])
	elif mode == 96:
		liz.addContextMenuItems(items = [("Excluir da lista", 'XBMC.RunPlugin({0}?url={1}&mode=355&iconimage={2}&name={3}&index={4})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name), index))])
	if mode == 10:
		urlParams['index'] = index
	u = '{0}?{1}'.format(sys.argv[0], urllib.urlencode(urlParams))
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)
	
def ListImdb(): #352
	file = os.path.join(addon_data_dir, 'imdb.txt')
	chList = common.ReadList(file)
	#chList = sorted(chList, key=lambda k: k['nome'], reverse=False)
	i = 0
	mg = metahandlers.MetaData()
	for channel in reversed(chList):
		if i == 100: break
		try:
			mm = mg.get_meta('movie', urllib.quote(channel["nome"].encode("utf-8")), tmdb_id=channel["id"])
			mm['tagline'] = mm['genre']
			#AddDir(mm['title'] + " / " + channel["name"].encode("utf-8"), channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"), metah=mm, DL="["+str(mm['rating'])+"]", index = i)
			#AddDir(channel["nome"] + " (" + channel["ano"]+")", channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"), metah=mm, DL="["+str(mm['rating'])+"]", index = i)
			mm['title'] = urllib.unquote(mm['title'].encode("utf-8"))
			AddDir(mm['title'] + " (" + str(channel["ano"])+")", channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"), metah=mm, DL="["+str(mm['rating'])+"]", index = i)
		except:
			pass
		i += 1
		
def ListImdbOut(): #353
	trak = traktM()
	#ST(trak)
	#AddDir("Reload" , "", 40, isFolder=False)
	cidi = "Português" if Cidi=="0" else "Inglês"
	AddDir("[COLOR green][B][Idioma]:[/B] "+ cidi +" (Clique para alterar)[/COLOR]" , "", 357, "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False)
	AddDir("[COLOR blue][B][Organizar por]:[/B] " + CImdb2[int(Cat2)]+"[/COLOR]", "", 356, isFolder=False)
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + Clista[int(Cat)] +"[/COLOR]", "" ,80 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False)
	file = common.OpenURL("http://cbplay.000webhostapp.com/imdb/imdb.txt")
	chList = json.loads(file)
	Idi = "name" if Cidi == "1" else "nome"
	if Cat2 == "0":
		chList = sorted(chList, key=lambda k: k[Idi], reverse=False)
	else:
		chList = sorted(chList, key=lambda k: (k[CImdb[int(Cat2)]], k[Idi]), reverse=True)
	mg = metahandlers.MetaData()
	for channel in chList:
		try:
			mm = mg.get_meta('movie', urllib.quote(channel[Idi].encode("utf-8")), tmdb_id=channel["id"])
			mm['tagline'] = mm['genre']
			if Clista[int(Cat)] in mm['genre'].encode("utf-8") or Cat=="0":
				mm['title'] = urllib.unquote(mm['title'].encode("utf-8"))
				pc = 1 if mm['imdb_id'] in trak else None
				#AddDir(mm['title'] + " (" + str(channel["ano"])+")", channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"), metah=mm, DL="["+str(mm['rating'])+"]", index = -1)
				AddDir(mm['title'] + " (" + str(channel["ano"])+")", channel["url"].encode("utf-8"), 97, "", mm['tmdb_id'], isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"), metah=mm, DL="", index = -1, playcount=pc)
				#AddDir(mm['title'] + " / " + channel["name"].encode("utf-8"), channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"), metah=mm, DL="["+str(mm['rating'])+"]", index = -1)
		except:
			#AddDir( str(channel["id"]), channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"))
			#AddDir( "[B][COLOR white]"+str(channel["id"]) + "[/B][/COLOR]", channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"))
			#ST(channel["id"])
			pass
			
def ImdbIdioma(): #357
	x2 = Addon.getSetting("Cidi")
	x = "0" if x2=="1" else "1"
	Addon.setSetting("Cidi", x)
	xbmc.executebuiltin("XBMC.Container.Refresh()")
	
def GenImdb(): #356
	d = xbmcgui.Dialog().select("Escolha o Genero", CImdb2)
	if d != -1:
		global Cat2
		Addon.setSetting("Cat2", str(d) )
		Cat2 = d
		xbmc.executebuiltin("XBMC.Container.Refresh()")
			
def Generos(): #80
	d = xbmcgui.Dialog().select("Escolha o Genero", Clista)
	if d != -1:
		global Cat
		Addon.setSetting("Cat", str(d) )
		Cat = d
		xbmc.executebuiltin("XBMC.Container.Refresh()")
		
def CleanCache(): #666
	AddDir("Reload" , "", 40, isFolder=False)
	d = xbmcgui.Dialog().input("Digite ok para confirmar e deletar o cache")
	if d != "ok":
		return
	cache = re.sub('addon_data.+', '', cacheDir )
	cachethumb = cache + "Thumbnails"
	cachedb = cache + "Database"
	Thumdir = ""
	for dirname, dirnames, filenames in os.walk(cachedb):
		try:
			for fn in filenames:
				#AddDir(str(fn) , "", 40, isFolder=False)
				if "extures" in fn:
					Thumdir = fn
		except:
			pass
	try:
		content = common.OpenURL("https://github.com/D4anielCB/texture/blob/master/Textures13.db?raw=true")
	except:
		NF("Não foi possível. Tente novamente mais tarde!")
		return
	try:
		os.unlink(cachedb+"\\"+Thumdir)
		NF("Cache limpo. reinicie o Kodi!")
	except OSError as e:
		try:
			py = cachedb+"\\"+Thumdir
			file = open(py, "w")
			file.write(content)
			file.close()
			NF("Reinicie o Kodi e refaça o procedimento")
		except OSError as e:
			NF("Erro")

	xbmc.sleep(2000)
	try:
		shutil.rmtree(cachethumb, ignore_errors=True)
	except:
		xbmcgui.Dialog().ok('Cube Play', "Erro 2!")
		pass
	
		
def Refresh():
	xbmc.executebuiltin("XBMC.Container.Refresh()")
	#Addon.setSetting("MUcache", "false" )
	#Addon.setSetting("MUcacheEpi", "false" )

def RemoveFromLists(i):
	index = int(i)
	#ST(index)
	listFile = os.path.join(addon_data_dir, 'imdb.txt')
	chList = common.ReadList(listFile)
	#chList = sorted(chList, key=lambda k: k['nome'], reverse=False)
	chList = list(reversed(chList))
	if index < 0 or index >= len(chList):
		return
	del chList[index]
	common.SaveList(listFile, list(reversed(chList)))
	xbmc.executebuiltin("XBMC.Container.Refresh()")

def Update(): #200
	Path = xbmc.translatePath( xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
	try:
		fonte = common.OpenURL( "https://raw.githubusercontent.com/D4anielCB/CBm/main/default.py" )
		prog = re.compile('#checkintegritycbmeta').findall(fonte)
		if prog:
			py = os.path.join( Path, "default.py")
			file = open(py, "w")
			file.write(fonte)
			file.close()
	except:
		pass
	NF("Atualizando...")
	xbmc.sleep(2000)
	
def ST(x="", o="w"):
	x = str(x)
	Path = xbmc.translatePath( xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
	py = os.path.join( Path, "study.txt")
	#file = open(py, "a+")
	file = open(py, o)
	file.write(x+"\n")
	file.close()

def NF(x, t=5000):
	xbmc.executebuiltin("Notification({0}, {1}, {3}, {2})".format(AddonName, str(x), icon, t))
	
def PlayFile(name, url):
	#url = re.sub('\.mp4$', '.mp4?play', url)
	url = common.getFinalUrl(url)
	#xbmc.log('--- Playing "{0}". {1}'.format(name, url), 2)
	#ST(url)
	listitem = xbmcgui.ListItem(path=url)
	#ST(metah)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
	
def AddSeek(id, gTime, totalTime):
	if id == "" or gTime < 1 or totalTime < 1 or not "tt" in id:
		return
	seek = str(100*gTime/totalTime)
	try:
		py = os.path.join(addon_data_dir, id+".txt")
		if int(float(seek)) > 5 and int(float(seek)) < 90:
			file = open(py, "w")
			file.write(seek)
			file.close()
		else:
			try:
				os.remove(py)
			except:
				pass
	except:
		pass

	
def ReadSeek(id):
	py = os.path.join(addon_data_dir, id+".txt")
	try:
		if os.path.exists(py):
			file = open(py, "r")
			c = file.read()
			file.close()
			return c
		else:
			return "0"
	except:
		return "0"
	
def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)
	
def Biblioteca(): #100
	if not "noupdate" in cFonte1:
		Update()
	else:
		#NF("nao deu update")
		pass
	if DirB == "":
		return
	try:
		link = common.OpenURL("http://cbplay.000webhostapp.com/imdb/imdb.txt")
		link2 = strip_accents(link)
		j=json.loads(link2)
	except:
		return
	if str( len(j) ) == Addon.getSetting("DirCount"):
		xbmc.sleep(1000)
		xbmc.executebuiltin('XBMC.UpdateLibrary(video)')
		return
	for x in j:
		try:
			t = x['name'].encode("utf-8").replace('&','e').replace(' ','_').replace('\'','').replace(':','').replace('?','').replace('*','')
			f = open(DirB+'/'+t+'_('+x['ano']+')'+x['url']+'.strm','wb')
			f.write('plugin://plugin.video.CubePlayMeta/?DL=&iconimage='+x['id']+'&index=&background=None&year=&info=&logos=&episode=&name=&url='+x['url']+'&cache=0&metah=%7B%7D&mode=97&playcount=None')
			f.close()
		except:
			f = open(DirB+'/V/'+x['id']+'.txt','wb')
			f.write('')
			f.close()
	Addon.setSetting("DirCount", str( len(j) )  )
	NF("Atualizando Biblioteca")
	xbmc.sleep(1000)
	xbmc.executebuiltin('XBMC.UpdateLibrary(video)')
	
def convert_size(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])
	
class XBMCPlayer( xbmc.Player ):
	def __init__( self ):
		self.totalTime = 1
		self.gTime = 1
		self.id = ""

	def onPlayBackStarted( self ):
        # Will be called when xbmc starts playing a file
		xbmc.log( "LED Status: Playback Started, LED ON" )

	def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
		xbmc.log( "LED Status: Playback Stopped, LED OFF" )

	def onPlayBackStopped( self ):
		#self.id = "1"
        # Will be called when user stops xbmc playing a file
		#if Ctrakt:
			#xbmc.sleep(1000)
			#baixarsf()
			#xbmc.executebuiltin("XBMC.Container.Refresh()")
		#AddSeek( self.id, str(100*self.gTime/self.totalTime) )
		#Biblioteca()
		xbmc.log( "LED Status: Playback Stopped, LED OFF" )

	def onPlayBackPaused ( self ):
		try:
			if "redecanaisAS" in xbmc.Player().getPlayingFile():
				NF(xbmc.Player().getVideoInfoTag().getIMDBNumber())
				AddSeek( xbmc.Player().getVideoInfoTag().getIMDBNumber(), xbmc.Player().getTime(), xbmc.Player().getTotalTime() )
		except:
			pass

	""""def onPlayBackSeek ( self, stime, offset ):
		try:
			self.totalTime = xbmc.Player().getTotalTime()
			self.gTime = xbmc.Player().getTime()
			self.id = xbmc.Player().getVideoInfoTag().getIMDBNumber()
		except:
			pass"""
			
params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))
url = params.get('url')
logos = params.get('logos', '')
name = params.get('name')
iconimage = params.get('iconimage')
cache = int(params.get('cache', '0'))
index = params.get('index')
move = int(params.get('move', '0'))
mode = int(params.get('mode', '0'))
info = params.get('info')
background = params.get('background')
DL = params.get('DL')
year = params.get('year')
metah = params.get('metah')
episode = params.get('episode')
playcount = params.get('playcount')

if mode == 0:
	Categories()
	setViewM()
elif mode == 3 or mode == 32:
	PlayUrl(name, url, iconimage, "", "")
	#PlayFile(name, url)
elif mode == 40:
	Refresh()
elif mode == 51:
	Series(cFonte1)
	setViewS()
elif mode == 52:
	Series(cFonte2)
	setViewS()
elif mode == 53:
	Series(cFonte3)
	setViewS()
elif mode == 61:
	ListSNC(background)
elif mode == 62:
	PlayS()
	setViewS()
elif mode == 69:
	Series2()
elif mode == 71:
	MoviesNC()
	setViewM()
elif mode == 78:
	ListMoviesNC()
	setViewS()
elif mode == 79:
	PlayMNC()
	setViewS()
elif mode == 80:
	Generos()
elif mode == 81:
	CategoryOrdem2(url)
#------------
elif mode == 135:
	TemporadasRC(index)
elif mode == 133:
	PlaySRC()
elif mode == 139:
	AllEpisodiosRC()
	setViewS2()
elif mode == 138:
	PlayNextRC()
#-------------
elif mode == 191:
	ListSMM(background)
	setViewS()
elif mode == 192:
	ListEpiMM(background)
elif mode == 194:
	PlaySMM()
elif mode == 200:
	Update()
	xbmc.executebuiltin("XBMC.Container.Refresh()")
elif mode == 300:
	Latest()
	setViewS2()
elif mode == 301:
	AllEpi()
	setViewS2()
elif mode == 302:
	Baixar()
	setViewS2()
elif mode == 303:
	moviedb()
elif mode == 305:
	Excluir()
elif mode == 308:
	Next_epi()
	setViewS2()
elif mode == 352:
	ListImdb()
	setViewM2()
elif mode == 353:
	ListImdbOut()
	setViewM2()
elif mode == 355:
	RemoveFromLists(index)
elif mode == 356:
	GenImdb()
elif mode == 357:
	ImdbIdioma()
elif mode == 96:
	PlayMRC2()
elif mode == 97:
	Elementum()
elif mode == 666:
	CleanCache()
elif mode == 100:
	xbmc.sleep(2000)
	Biblioteca()
elif mode == 101:
	Addon.setSetting("DirCount", "0")
	xbmc.sleep(2000)
	Biblioteca()
elif mode == 401:
	ListSSF()
elif mode == 402:
	ListEpiSF()
	setViewS2()
elif mode == 405:
	PlaySSF()
elif mode == 409:
	LatestSSF()
	setViewS2()
elif mode == 500: #anime
	listanimevis()
	setViewS()
elif mode == 501: #anime
	listseavis()
	setViewS()
elif mode == 502: #anime
	animeepisvis()
	setViewS2()
elif mode == 503: #playanime
	playanimevis()
elif mode == 504: 
	playanimenextvis()
xbmcplugin.endOfDirectory(int(sys.argv[1]))
#checkintegritycbmeta
