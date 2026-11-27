-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SAEP
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SAEP
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SAEP` DEFAULT CHARACTER SET utf8 ;
USE `SAEP` ;

-- -----------------------------------------------------
-- Table `SAEP`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAEP`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(45) NULL,
  `senha` VARCHAR(45) NULL,
  PRIMARY KEY (`idusuario`),
  UNIQUE INDEX `login_UNIQUE` (`login` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAEP`.`responsavel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAEP`.`responsavel` (
  `idresponsavel` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `cpf` VARCHAR(200) NULL,
  PRIMARY KEY (`idresponsavel`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAEP`.`aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAEP`.`aluno` (
  `idaluno` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `responsavel_idresponsavel` INT NOT NULL,
  PRIMARY KEY (`idaluno`),
  INDEX `fk_aluno_responsavel1_idx` (`responsavel_idresponsavel` ASC) VISIBLE,
  CONSTRAINT `fk_aluno_responsavel1`
    FOREIGN KEY (`responsavel_idresponsavel`)
    REFERENCES `SAEP`.`responsavel` (`idresponsavel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAEP`.`matricula`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAEP`.`matricula` (
  `idmatricula` INT NOT NULL AUTO_INCREMENT,
  `curso` VARCHAR(45) NULL,
  `data` DATE NULL,
  `aluno_idaluno` INT NOT NULL,
  PRIMARY KEY (`idmatricula`),
  INDEX `fk_matricula_aluno1_idx` (`aluno_idaluno` ASC) VISIBLE,
  CONSTRAINT `fk_matricula_aluno1`
    FOREIGN KEY (`aluno_idaluno`)
    REFERENCES `SAEP`.`aluno` (`idaluno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
