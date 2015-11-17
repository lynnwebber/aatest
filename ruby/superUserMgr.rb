#!/usr/bin/env ruby

require 'rubygems'
require 'thor'
require 'bcrypt'
require 'pg'

# ------------- general use functions
def make_password_hash(inpasswd)
    a_password = BCrypt::Password.create(inpasswd)
    printf "Hashes to desired password? -> %s\n", a_password == inpasswd
    return a_password
end

# ------------ class for db management
class DBManager
    # create connection
    def connect
        @conn = PG.connect(
            :dbname => 'lynn',
            :user => 'lynn'
            #:password => '[password]'
        )
    end

    # create prepared statement methods
    def prepAddUser
        sql = %{
            INSERT INTO users
            (status,type,email,password_hash)
            VALUES
            ($1,$2,$3,$4)
        }
        @conn.prepare("add_user",sql)
    end

    def prepResetStatus
        sql = %{
            UPDATE users
            SET status = $2
            WHERE email = $1
        }
        @conn.prepare("reset_status",sql)
    end

    def prepResetPassword
        sql = %{
            UPDATE users
            SET password_hash = $2
            WHERE email = $1
        }
        @conn.prepare("reset_password",sql)
    end

    def prepListSuperUsers
        sql = %{
            SELECT * FROM users
            WHERE type = 'superadmin'
            AND status = $1
        }
        @conn.prepare("list_superusers",sql)
        sql = %{
            SELECT * FROM users
            WHERE type = 'superadmin'
        }
        @conn.prepare("list_all_superusers",sql)
    end

    # insert and update methods
    def addUser(stat,typ,email,pwhash)
        @conn.exec_prepared("add_user",[stat,typ,email,pwhash])
    end

    def resetStatus(email,stat)
        @conn.exec_prepared("reset_status",[email,stat])
    end

    def resetPassword(email,pwhash)
        @conn.exec_prepared("reset_password",[email,pwhash])
    end

    # query methods
    def listSuperusers(stat)
        @conn.exec_prepared("list_superusers",[stat])
    end

    def listAllSuperusers()
        @conn.exec("SELECT * FROM users where type = 'superadmin'")
    end

    # disconnect
    def disconnect
        @conn.close
    end
end


# ------------- the command line interface -----------
# thor is a very cool command line interface toolset
#
class Reset < Thor
    desc "status" ,"set users status"
    method_option :email,:default => "",:required => true,:aliases => "-e",:desc => "user email address for login (required)"
    method_option :status,:default => "",:required => true,:aliases => "-s",:desc => "user status: active or disabled"
    def status
      puts "status #{options.inspect}"
      dbm = DBManager.new()
      dbm.connect
      begin
          dbm.prepResetStatus
          dbm.resetStatus(options["email"],options["status"])
      rescue Exception => e
          puts e.message
          puts e.backtrace.inspect
      ensure
          dbm.disconnect
      end
    end

    desc "password" ,"reset users password"
    method_option :email,:default => "",:required => true,:aliases => "-e",:desc => "user email address for login (required)"
    method_option :passwd,:default => "",:required => true,:aliases => "-p",:desc => "user password (required)"
    def password
      puts "password #{options.inspect}"
      pwhash = make_password_hash(options["passwd"])
      puts "hash generated: #{pwhash}"
      dbm = DBManager.new()
      dbm.connect
      begin
          dbm.prepResetPassword
          dbm.resetPassword(options["email"],pwhash)
      rescue Exception => e
          puts e.message
          puts e.backtrace.inspect
      ensure
          dbm.disconnect
      end
    end
end


class SuperUser < Thor
  desc "add", "add superuser"
  method_option :status,:default => "active", :aliases => "-s",:desc => "user status: active or disabled"
  method_option :email,:default => "",:required => true,:aliases => "-e",:desc => "user email address for login (required)"
  method_option :type,:default => "superadmin",:aliases => "-t",:desc => "user type: superadmin, admin, regular, restricted"
  method_option :passwd,:default => "",:required => true,:aliases => "-p",:desc => "user password (required)"
  def add
      puts "add #{options.inspect}"
      pwhash = make_password_hash(options["passwd"])
      puts "hash generated: #{pwhash}"
      dbm = DBManager.new()
      dbm.connect
      begin
          dbm.prepAddUser
          dbm.addUser(options["status"],options["type"],options["email"],pwhash)
      rescue Exception => e
          puts e.message
          puts e.backtrace.inspect
      ensure
          dbm.disconnect
      end
  end

  desc "reset SUBCOMMAND ...ARGS", "reset users status or password"
  subcommand "reset", Reset

  desc "list" ,"list superusers"
  method_option :status,:default => "active", :aliases => "-s",:desc => "user status: active, disabled, any"
  def list
    puts "list #{options.inspect}"
    dbm = DBManager.new()
    dbm.connect
    if options["status"].upcase == "ANY"
        dbm.prepListSuperUsers
        res = dbm.listAllSuperusers()
        res.each do |row|
            puts row['email'] + ' --> ' + row["status"]
        end
    else
        dbm.prepListSuperUsers
        res = dbm.listSuperusers(options["status"])
        res.each do |row|
            puts row['email'] + ' --> ' + row["status"]
        end
    end
    dbm.disconnect
  end

end

# ---- main
def main
    SuperUser.start
end

# ---- run main
main
