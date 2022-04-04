%------------- PLANTILLA PAC EIMT. VERSIO 3 --------------
%--------------- Identificació --------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{PlantillaPACnova_Est}
\RequirePackage[utf8x]{inputenc}
\RequirePackage{ifthen}
\RequirePackage[dvips]{graphicx}
\RequirePackage{url}
\RequirePackage{fancyhdr}
\RequirePackage{color}
\RequirePackage[usenames,dvipsnames]{xcolor}

%% ----------------------- Opcions d'entrada pròpies del paquet: català, castellà o anglès-----
\newboolean{langspanish}
\newboolean{langcatalan}
\newboolean{langenglish}
\newboolean{practica}
\DeclareOption{CAT}{
\setboolean{langcatalan}{true}
\setboolean{langspanish}{false}
\setboolean{langenglish}{false}
} 
\DeclareOption{IB}{
\setboolean{langcatalan}{false}
\setboolean{langspanish}{true}
\setboolean{langenglish}{false}
}
\DeclareOption{ENG}{
\setboolean{langcatalan}{false}
\setboolean{langspanish}{false}
\setboolean{langenglish}{true}
}
\DeclareOption{practica}{\setboolean{practica}{true}}


\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}% Passa les opcions no declarades explícitament a "article". Així es poden fer servir totes les opcions d'article.
\ProcessOptions

%% --------------- Es carrega el paquet Babel -------------------
%\RequirePackage{babel}

%% --------------- Basat en l'estil article -------------------

\LoadClass[10pt]{article}

%% --------------- Configuració de la pàgina -------------------
\textwidth=15truecm
\textheight=17truecm
\oddsidemargin=1truecm
%\hoffset=-1truecm
\voffset=-0.5truecm
\parindent=0pt
\parskip=10pt
%% -------------- Paquets d'idioma -------------------------

\ifthenelse{\boolean{langspanish}}
		{\usepackage[spanish]{babel}}
{}\ifthenelse{\boolean{langcatalan}}
		{\usepackage[catalan]{babel}}			
{}\ifthenelse{\boolean{langenglish}}
		{\usepackage[english]{babel}}{}


%% --------------- Capçalera -------------------

\pagestyle{fancy} 
%\fancyhf{}
\setlength\headheight{35pt}
\lhead{\raisebox{0.075truecm}{\includegraphics[height=1truecm]{noulogo.png}}}
\fancyfoot{}
\renewcommand\headrulewidth{0pt}
\renewcommand\footrulewidth{1pt}
\renewcommand{\footrule}{\hbox to\headwidth{%
  \color{airblueuoc}\leaders\hrule height \footrulewidth\hfill}}
%\lfoot{\includegraphics[height=0.35truecm,keepaspectratio=true]{noulogo.png}}
\lfoot{}
\rfoot{\includegraphics[height=0.35truecm,keepaspectratio=true]{eimt.png} \hspace*{0.25truecm} \thepage}

%% --------------- Definició de comandes -------------------
%\newcommand{\bluepac}{\color{airblueuoc}} %% Definició del color blau de la plantilla.
\definecolor{airblueuoc}{rgb}{0.36, 0.54, 0.66}
\newcommand{\bluepac}{\color{airblueuoc}} %% Definició del color blau de la plantilla.
\newcommand{\graypac}{\color{gray}} %% Definició del color gris de la plantilla.
\newcommand{\sectionblue}[1]{\section*{\bluepac #1}}
\newcommand{\subsectiongray}[1]{\section*{\graypac #1}}
\newcommand{\HRule}{\noindent\rule{\linewidth}{1.5pt}}
\newcommand{\Hrule}{\noindent\rule{\linewidth}{0.75pt}}
%{\color{airblueuoc}\hrule}
%\newcommand{\headrulecolor}[4]{\patchcmd{\headrule}{\hrule}{\color{#1}\hrule}{}{}}
%\renewcommand{\headrulewidth}{2pt}% 2pt header rule
%\renewcommand{\headrule}{\hbox to\headwidth{\color{headercolor}\leaders\hrule height \headrulewidth\hfill}}

%% ----------------------- Generació d'elements propis de la PAC -----------------------------
\newcommand{\textinicial}[6] 
{
	
	%\tiny{
%		\begin{tabular}{l@{}}
%			\ifthenelse{\boolean{langspanish}}
%			{Curso #3 \\Semestre #4}
%			{}\ifthenelse{\boolean{langcatalan}}
%			{Curs #3 \\Semestre #4}
%			{}\ifthenelse{\boolean{langenglish}}
%			{Course #3 \\Semester #4}{}
%		\end{tabular}}}
	
	{\rhead{
    \scriptsize{{\bluepac #1 · #2 ·#3 \\#4 · #5 \\\,\\  
    \large \textcolor{black}{#6}
    }}\\
	%\includegraphics[height=1.75truecm,keepaspectratio=true]{logoeimt.png}
}
}
	{}
	{}

%%	\HRule
}
\newcommand{\infopac}[8]
{
\ifthenelse{\boolean{langspanish}}
	{
\sectionblue{Presentación}
#1
\sectionblue{\color{airblueuoc}Competencias}
#2
\sectionblue{\color{airblueuoc}Objetivos}
#3
\sectionblue{\color{airblueuoc}Descripción de la \ifthenelse{\boolean{practica}}{Pràctica}{PEC} a realizar} 
#4
\sectionblue{\color{airblueuoc}Recursos}
\subsectiongray{Recursos Básicos}
#5
\subsectiongray{Recursos Complementarios}
#6
\sectionblue{\color{airblueuoc}Criterios de valoración}
#7
\sectionblue{\color{airblueuoc}Formato y fecha de entrega}
#8	
	}
	{}
	\ifthenelse{\boolean{langcatalan}}
	{

\sectionblue{Presentació}
#1
\sectionblue{\color{airblueuoc}Competències}
#2
\sectionblue{\color{airblueuoc}Objectius}
#3
\sectionblue{\color{airblueuoc}Descripció de la \ifthenelse{\boolean{practica}}{Pràctica}{PAC}} 
#4
\sectionblue{\color{airblueuoc}Recursos}
\subsectiongray{Recursos Bàsics}
#5
\subsectiongray{Recursos Complementaris}
#6
\sectionblue{\color{airblueuoc}Criteris d'avaluació}
#7
\sectionblue{\color{airblueuoc}Format i data de lliurament}
#8
	}{}
	\ifthenelse{\boolean{langenglish}}
	{
	\sectionblue{Presentation}
#1
\sectionblue{\color{airblueuoc}Competences}
#2
\sectionblue{\color{airblueuoc}Objectives}
#3
\sectionblue{\color{airblueuoc}Description of the \ifthenelse{\boolean{practica}}{Practical Activity}{CAT} to do} 
#4
\sectionblue{\color{airblueuoc}Resources}
\subsectiongray{Basic Resources}
#5
\subsectiongray{Additional Resources}
#6
\sectionblue{\color{airblueuoc}Evaluation criteria}
#7
\sectionblue{\color{airblueuoc}Format and date of delivery}
#8
	}{}
}
%% ---------------------- Definicions de preguntes i qüestions-----------------------
\newcommand{\solucions}
{
	{\sectionblue{\ifthenelse{\boolean{langspanish}}
		{Soluciones}
		{}\ifthenelse{\boolean{langcatalan}}
		{Solucions}
		{}\ifthenelse{\boolean{langenglish}}
		{Solutions}{}
		}}
	\Hrule \\
}

\newcommand{\enunciats}
{
	{\sectionblue{\ifthenelse{\boolean{langspanish}}
		{Enunciados}
		{}\ifthenelse{\boolean{langcatalan}}
		{Enunciats}
		{}\ifthenelse{\boolean{langenglish}}
		{Problem statement}{}
		}}
	\Hrule \\
}

\relax
