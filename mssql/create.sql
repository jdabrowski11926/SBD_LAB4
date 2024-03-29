CREATE DATABASE SBD_LAB_4
GO

USE [SBD_LAB_4]
GO
/****** Object:  Table [dbo].[Actor]    Script Date: 21.06.2019 18:18:35 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Actor](
	[id] [numeric](18, 0) NOT NULL,
	[firstName] [varchar](50) NULL,
	[lastName] [varchar](50) NULL,
	[birthDate] [date] NULL,
 CONSTRAINT [PK_Actor] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Category]    Script Date: 21.06.2019 18:18:35 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Category](
	[id] [numeric](18, 0) NOT NULL,
	[name] [varchar](50) NULL,
	[description] [varchar](50) NULL,
 CONSTRAINT [PK_Category] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Director]    Script Date: 21.06.2019 18:18:35 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Director](
	[id] [numeric](18, 0) NOT NULL,
	[firstName] [varchar](50) NULL,
	[lastName] [varchar](50) NULL,
	[birthDate] [date] NULL,
 CONSTRAINT [PK_Director] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Movie]    Script Date: 21.06.2019 18:18:35 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Movie](
	[id] [numeric](18, 0) NOT NULL,
	[name] [varchar](50) NULL,
	[Director] [numeric](18, 0) NULL,
	[releaseDate] [date] NULL,
	[Category] [numeric](18, 0) NULL,
	[length] [numeric](18, 0) NULL,
	[budget] [float] NULL,
	[rating] [float] NULL,
 CONSTRAINT [PK_Movie] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Role]    Script Date: 21.06.2019 18:18:35 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Role](
	[idMovie] [numeric](18, 0) NOT NULL,
	[idActor] [numeric](18, 0) NOT NULL,
	[characterName] [varchar](50) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Movie]  WITH CHECK ADD  CONSTRAINT [FK_Movie_Category] FOREIGN KEY([Category])
REFERENCES [dbo].[Category] ([id])
GO
ALTER TABLE [dbo].[Movie] CHECK CONSTRAINT [FK_Movie_Category]
GO
ALTER TABLE [dbo].[Movie]  WITH CHECK ADD  CONSTRAINT [FK_Movie_Director] FOREIGN KEY([Director])
REFERENCES [dbo].[Director] ([id])
GO
ALTER TABLE [dbo].[Movie] CHECK CONSTRAINT [FK_Movie_Director]
GO
ALTER TABLE [dbo].[Role]  WITH CHECK ADD  CONSTRAINT [FK_Role_Actor] FOREIGN KEY([idActor])
REFERENCES [dbo].[Actor] ([id])
GO
ALTER TABLE [dbo].[Role] CHECK CONSTRAINT [FK_Role_Actor]
GO
ALTER TABLE [dbo].[Role]  WITH CHECK ADD  CONSTRAINT [FK_Role_Movie] FOREIGN KEY([idMovie])
REFERENCES [dbo].[Movie] ([id])
GO
ALTER TABLE [dbo].[Role] CHECK CONSTRAINT [FK_Role_Movie]
GO
