from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate  # For prompts
from langchain_ollama import ChatOllama
from langchain_openai.chat_models import (
    ChatOpenAI,
)  # For interacting with Open AI's chat model interface like gpt 4 etc

load_dotenv()


def main():
    infomation = """
    Roger Federer born 8 August 1981) is a Swiss former professional tennis player. He was ranked as the world No. 1 in men's singles by the Association of Tennis Professionals (ATP) for 310 weeks (second-most of all time), including a record 237 consecutive weeks, and finished as the year-end No. 1 five times. Federer won 103 singles titles on the ATP Tour, the second most since the start of the Open Era in 1968, including 20 major men's singles titles (among which a record eight men's singles Wimbledon titles, and an Open Era joint-record five men's singles US Open titles) and six year-end championships.

For nearly two decades, Federer was a leading figure in men's tennis alongside Rafael Nadal and Novak Djokovic, collectively known as the Big Three. A Wimbledon junior champion in 1998 and former ball boy, Federer won his first major singles title at Wimbledon in 2003 at age 21.[3] For the next several years Federer was the dominant player in men's tennis, playing in 20 out of 24 major singles finals between 2004 and 2009. He won three of the four majors and the Tour Finals in 2004, 2006, and 2007, as well as five consecutive titles at both Wimbledon and the US Open. Federer completed the career Grand Slam at the 2009 French Open after three consecutive runner-up finishes to Nadal, his main rival until 2010. At age 27, he surpassed Pete Sampras's record of 14 major men's singles titles at Wimbledon in 2009.

Federer and Stan Wawrinka led the Switzerland Davis Cup team to their first title in 2014, following their Olympic doubles gold victory at the 2008 Beijing Olympics. He also won a silver medal in singles at the 2012 London Olympics, finishing runner-up to Andy Murray. After a half-year hiatus in 2016 to recover from knee surgery, Federer returned to tennis, winning three more majors over the next two years, including the 2017 Australian Open over Nadal and a record eighth singles title at the 2017 Wimbledon Championships. At the 2018 Australian Open, Federer became the first man to win 20 major singles titles and shortly after the oldest ATP world No. 1 at the time, at age 36. In September 2022, he retired from professional tennis following the Laver Cup.

A versatile all-court player, Federer's grace on the court made him popular among tennis fans.[4][5] Originally lacking self-control as a junior,[6] he transformed his on-court demeanor[7] to become well-liked for his graciousness, winning the Stefan Edberg Sportsmanship Award 13 times. He also won the Laureus World Sportsman of the Year award a joint-record five times. Outside of competition, Federer played an instrumental role in the creation of the Laver Cup team competition. He is also an active philanthropist. He established the Roger Federer Foundation, which targets impoverished children in southern Africa, and has raised funds in part through the Match for Africa exhibition series. By the end of his career, Federer was routinely one of the top-ten highest-paid athletes in any sport, and ranked first among all athletes with $100 million in endorsement income in 2020.[8]
"""
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template="""
    Given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
""",
    )

    llm = ChatOllama(model="gpt-oss:latest", temperature=0)

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": infomation})

    print(response.content)


if __name__ == "__main__":
    main()
